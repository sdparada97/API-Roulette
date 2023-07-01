from api.database import db
from enum import Enum

class TypeBet(Enum):
    NUMBER = 'NUMERIC'
    COLOR = 'COLOR'

class Color(Enum):
    RED = 'ROJO'
    BLACK = 'NEGRO'

class Bet(db.Model):
    __tablename__ = 'bets'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    roulette_id = db.Column(db.Integer, db.ForeignKey('roulettes.id'))
    roulette = db.relationship("Roulette",back_populates="bets")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User",back_populates="bets")
    type_bet = db.Column(db.Enum(TypeBet,values_callable=lambda x: [str(e.value) for e in TypeBet]),nullable=False)
    color_bet = db.Column(db.Enum(Color,values_callable=lambda x: [str(e.value) for e in Color]))
    number_bet = db.Column(db.Integer)
    bet_amount = db.Column(db.Numeric(), nullable=False)
    is_wins = db.Column(db.Boolean(),default=False)
    amount_won = db.Column(db.Numeric(), nullable=False, default=0)
    
    def __repr__(self):
        return f"<Bet {self.id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()