from app import db


class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome_completo = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    data_de_cadastro = db.Column(db.Date)
    checkInUser = db.relationship("CheckIn", backref="users", lazy=True)

    def __init__(self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf
