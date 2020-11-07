import re
from datetime import date

from flask import jsonify

from app import db
from app.user.models import User
from app.user import schemas as user_schemas

schema = user_schemas.UserSchema()


def register_user(user: list):
    user.cpf = format_cpf(user.cpf)
    try:
        user_object = save_user(user)
        return jsonify(schema.dump(user_object))
    except Exception:
        return {"message": "Internal Error"}, 500


def search_user(id_user: int) -> User:
    return User.query.filter_by(id_user=id_user).first()


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(id_user: int) -> bool:
    user_found = search_user(id_user)
    if user_found:
        db.session.delete(user_found)
        db.session.commit()
        return {"message": "User successfully deleted"}, 200
    return {"message": "User not Found"}, 404


def updade_user(id_user: int, update: dict):
    user_found = search_user(id_user)
    scheme_update = user_schemas.UpdateUserSchema()

    if user_found:
        for key, value in update.items():
            if key == "nome_completo":
                user_found.nome_completo = value
            elif key == "email":
                user_found.email = value
            elif key == "cpf":
                user_found.cpf = value
        db.session.commit()
        return jsonify(scheme_update.dump(user_found))
    return {"message": "User not Found"}, 404


def find_exist_user_cpf(cpf: str) -> bool:
    return db.session.query(
        User.query.filter_by(cpf=format_cpf(cpf)).exists(),
    ).scalar()


def format_cpf(cpf):
    return re.sub("[^0-9]", "", cpf)


def find_user(id_user: int) -> User:
    user = search_user(id_user)
    if user:
        return jsonify(schema.dump(user)), 200
    return {"message": "User not Found"}, 404
