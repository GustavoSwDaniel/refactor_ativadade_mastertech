from app import db


class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome_completo = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    data_de_cadastro = db.Column(db.Date)
    checkInUser = db.relationship("CheckIn", backref="users", lazy=True)


class CheckIn(db.Model):

    __tablename__ = "checks"

    id_pont = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_responsavel = db.Column(db.String(255))
    tipo_da_batida = db.Column(db.String(30))
    data_hora_batida = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id_user"))
