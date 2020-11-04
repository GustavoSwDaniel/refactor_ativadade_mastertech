from datetime import date
from app import db
from app.user.models import User


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def find_user(id_user: int):
    return User.query.filter_by(id_user=id_user).first()


def find_exist_user_cpf(cpf: str) -> bool:
    verificacao = User.query.filter_by(cpf=cpf).first()
    if verificacao:
        return False
    return True


def delete_user(id_user: int) -> bool:
    user_found = find_user(id_user)
    if user_found:
        db.session.delete(user_found)
        db.session.commit()
        return True
    return False


def updade_user(id_user: int, field: dict):
    if len(field) <= 3:
        user_found = find_user(id_user)
        print(user_found)
        if user_found:
            db.session.commit()
            return True
        return False
    return False
