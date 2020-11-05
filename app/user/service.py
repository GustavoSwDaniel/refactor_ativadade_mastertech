from datetime import date
from app import db
from app.user.models import User


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def find_user(id_user: int) -> User:
    return User.query.filter_by(id_user=id_user).first()


def find_exist_user_cpf(cpf: str) -> bool:
    verification = User.query.filter_by(cpf=cpf).first()
    if verification:
        return False
    return True


def delete_user(id_user: int) -> bool:
    user_found = find_user(id_user)
    if user_found:
        db.session.delete(user_found)
        db.session.commit()
        return True
    return False


def updade_user(id_user: int, update: dict):
    user_found = find_user(id_user)

    if user_found:
        for key, value in update.items():
            if key == "nome_completo":
                user_found.nome_completo = value
            elif key == "email":
                user_found.email = value
            elif key == "cpf":
                user_found.cpf = value
        db.session.commit()
        return user_found
    return False
