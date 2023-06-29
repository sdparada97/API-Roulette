from api.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(45),nullable=False)
    password_hash = db.Column(db.Text(), nullable=False)
    available_credit = db.Column(db.Numeric(),default=0, nullable=False)
    bets = db.relationship('Bet', back_populates="user")
    
    def __init__(self, email,password_hash,available_credit):
        self.email = email
        self.password_hash = password_hash
        self.available_credit = available_credit
    
    def __repr__(self):
        return f"<User {self.id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()