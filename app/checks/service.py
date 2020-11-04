from datetime import datetime

from app import db
from app.checks.models import CheckIn
from app.user.service import find_user


def register_check_User(id_user: int, point_data: CheckIn):
    point_data.data_hora_batida = datetime.now()
    user = find_user(id_user)
    if user:
        point_data.user_id = id_user
        db.session.add(point_data)
        db.session.commit()
        return point_data
    return False
