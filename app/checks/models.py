from app import db


class CheckIn(db.Model):
    __tablename__ = "checks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    responsible_user = db.Column(db.String(255))
    point_type = db.Column(db.String(30))
    point_date_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
