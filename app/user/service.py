from flask import jsonify

from app import db
from app.user.models import User
from datetime import date


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def show_user():
    return [jsonify(User) for User in User.query.all()]
