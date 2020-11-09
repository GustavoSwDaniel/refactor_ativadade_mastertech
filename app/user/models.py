from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    full_name = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    registration_date = db.Column(db.Date)
    checkInUser = db.relationship("CheckIn", backref="users", lazy=True)
