from api.database import db
from enum import Enum
import sqlalchemy as sa

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
                            default=RouletteStatus.OPEN)
    
    def __init__(self):
        self.total_bet = 0
        self.is_active = RouletteStatus.OPEN.value
    
    def __repr__(self):
        return f"<Roulette {self.id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()