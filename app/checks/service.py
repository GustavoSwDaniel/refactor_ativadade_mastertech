from datetime import datetime

from app import db
from app.checks.models import CheckIn
from app.user.service import find_user
from app.checks import schemas as check_schemas

schemas = check_schemas.CheckSchema()

FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


def register_check_User(id_user: int, point_data: CheckIn):
    point_data.data_hora_batida = datetime.now()
    user = find_user(id_user)
    if user:
        point_data.user_id = id_user
        db.session.add(point_data)
        db.session.commit()
        return point_data
    return False


def worked_hour(id_user: int):
    user = find_user(id_user)
    if user:
        user_dados = read_checks_dada(id_user)

        work_hours = []
        for hours in user_dados:
            if "data_hora_batida" in hours:
                work_hours.append(hours["data_hora_batida"])
        work_hours.sort()
        total_hours = calculate_hours(work_hours)
        return total_hours[0:7]
    return False


def calculate_hours(work_hours: list) -> str:
    size = len(work_hours)
    hours = datetime(1, 1, 1, 0, 0, 0)

    if size % 2 == 0:
        for i in range(0, size, 2):
            entry = datetime.strptime(work_hours[i], FORMAT)
            out = datetime.strptime(work_hours[i + 1], FORMAT)
            hours = out - entry
        hours = str(hours)
        return hours
    else:
        work_hours.pop()
        calculate_hours(work_hours)


def validadete_entrada(type_point: str, id_user: int) -> bool:

    print(type_point)
    last_check = read_checks_dada(id_user)
    last_check = last_check[-1]
    if last_check["tipo_da_batida"] == "Saida" and type_point == "Saida":
        return False
    elif last_check["tipo_da_batida"] == "Entrada" and type_point == "Entrada":
        return False
    else:
        return True


def read_checks_dada(id_user):
    return [
        schemas.dump(user_date)
        for user_date in CheckIn.query.filter_by(user_id=id_user)
    ]
