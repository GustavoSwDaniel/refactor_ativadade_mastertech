from flask import jsonify
from datetime import date

import re
from app import db
from app.user.models import User
from app.user import schemas as user_schemas


schema = user_schemas.UserSchema()


def register_user(user: list):
    validation_cpf = ValidateCPF(user.cpf)
    if find_exist_user_cpf(cpf=user.cpf):
        if validation_cpf.validation():
            try:
                user_object = save_user(user)
                return jsonify(schema.dump(user_object))
            except Exception:
                return {"message": "Internal Error"}, 500
            return {"message": "CPF invalid"}, 404
    return {"message": "CPF already registered"}, 404


def search_user(id_user: int) -> User:
    return User.query.filter_by(id_user=id_user).first()


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def find_user(id_user: int) -> User:
    user = search_user(id_user)
    if user:
        return jsonify(schema.dump(user)), 200
    return {"message": "User not Found"}, 404


def find_exist_user_cpf(cpf: str) -> bool:
    verification = User.query.filter_by(cpf=cpf).first()
    if verification:
        return False
    return True


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


class ValidateCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def validation(self):
        if not self.cpf:
            return False

        new_cpf = self._calcula_digitos(self.cpf[:9])
        new_cpf = self._calcula_digitos(new_cpf)

        if new_cpf == self.cpf:
            return True
        return False

    @staticmethod
    def _calcula_digitos(cpf):
        if not cpf:
            return False

        sequence = cpf[0] * len(cpf)

        if sequence == cpf:
            return False
        soma = 0
        for key, multiplier in enumerate(range(len(cpf) + 1, 1, -1)):
            soma += int(cpf[key]) * multiplier

        rest = 11 - (soma % 11)
        rest = rest if rest <= 9 else 0
        return cpf + str(rest)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._clear_cpf(cpf)

    @staticmethod
    def _clear_cpf(cpf):
        return re.sub("[^0-9]", "", cpf)
