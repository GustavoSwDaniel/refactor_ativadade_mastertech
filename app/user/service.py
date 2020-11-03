from app import db
from app.user.models import User
from app.user.schemas import UserSchema


def save_user(user: User) -> User:
    user.data_de_cadastro = date.today()
    db.session.add(user)
    db.session.commit()
    return user


def show_user():
    userSchema = UserSchema()
    return [userSchema.dump(User) for User in User.query.all()]


def find_user(id_user):
    user = User.query.filter_by(id_user=id_user).first()
    if user:
        return user, 200
    return "User not Found", 404
