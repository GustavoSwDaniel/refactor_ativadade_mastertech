from app import db


class CheckIn(db.Model):
    __tablename__ = "checks"

    id_pont = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_responsavel = db.Column(db.String(255))
    tipo_da_batida = db.Column(db.String(30))
    data_hora_batida = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id_user"))
