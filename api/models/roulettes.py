from api.database import db
from decimal import Decimal
from enum import Enum

from ..models.bets import Bet, TypeBet
from ..models.users import User

class RouletteStatus(Enum):
    OPEN = 'ABIERTA'
    CLOSE = 'CERRADA'

class Roulette(db.Model):
    __tablename__ = 'roulettes'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    bets = db.relationship('Bet',back_populates="roulette")
    total_bet = db.Column(db.Numeric(),default=0, nullable=False)
    is_active = db.Column(db.Enum(RouletteStatus,
                                    values_callable=lambda x: [str(e.value) for e in RouletteStatus]),
                            default=None)
    
    def __init__(self):
        self.total_bet = 0
    
    def __repr__(self):
        return f"<Roulette {self.id}>"
    
    def get_total_bets(self):
        self.total_bet = sum(bet.bet_amount for bet in self.bets)
        return self.total_bet
    
    def get_roulette_result(self,num_wins,color_wins):
        roulette_results = []
        for bet in self.bets:
            if isinstance(bet,Bet):
                user = User.query.filter_by(id=bet.user_id).first()
                if isinstance(user,User):
                    if bet.type_bet == TypeBet.COLOR:
                        print(bet.color_bet)
                        if bet.color_bet.value == color_wins:
                            bet.is_wins = True
                            bet.amount_won = bet.bet_amount * Decimal(1.8)
                            user.available_credit += bet.amount_won
                            bet.save()
                        else:
                            user.available_credit -= bet.bet_amount
                        user.save()
                        roulette_results.append({
                            "id": bet.id,
                            "color": bet.color_bet.value,
                            "is_wins": bet.is_wins,
                            "bet_amount": bet.amount_won
                        })
                    if bet.type_bet == TypeBet.NUMBER:
                        if bet.number_bet == num_wins:
                            bet.is_wins = True
                            bet.amount_won = bet.bet_amount * Decimal(5)
                            user.available_credit += bet.amount_won
                            bet.save()
                        else:
                            user.available_credit -= bet.bet_amount
                        user.save()
                        roulette_results.append({
                            "id": bet.id,
                            "number": bet.number_bet,
                            "is_wins": bet.is_wins,
                            "bet_amount": bet.amount_won
                        })
        return roulette_results
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        