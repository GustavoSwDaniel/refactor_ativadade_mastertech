from datetime import datetime

from flask import jsonify

from app import db
from app.checks.models import CheckIn
from app.user.service import find_user
from app.checks import schemas as check_schemas

schemas = check_schemas.CheckSchema()

FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


def register_check_User(id_user: int, point_data: CheckIn):
    point_data.point_date_time = datetime.now()
    user = find_user(id_user)

    if user:
        check_user = schemas.dump(point_data)
        validate = validadete_check(
            check_user["point_type"],
            id_user,
        )
        if validate:
            point_data.user_id = id_user
            db.session.add(point_data)
            db.session.commit()
            return jsonify(schemas.dump(point_data)), 201
        return {"message": "<Tipo de Entrada> repeated"}, 400
    return {"message": "User not found"}, 404


def worked_hour(id_user: int):
    user = find_user(id_user)
    if user:
        user_dadas = read_checks_dada(id_user)

        work_hours = []
        for hours in user_dadas:
            if "point_date_time" in hours:
                work_hours.append(hours["point_date_time"])
        work_hours.sort()
        total_hours = calculate_hours(work_hours)
        return jsonify(
            {"Total de Horas trabalhadas": total_hours},
            [
                schemas.dump(check)
                for check in CheckIn.query.filter_by(user_id=id_user).all()
            ],
        )
    return {"message": "User not found"}, 404


def calculate_hours(work_hours: list) -> str:
    size = len(work_hours)
    hours = datetime(1, 1, 1, 0, 0, 0)

    if size % 2 == 0:
        for i in range(0, size, 2):
            entry = datetime.strptime(work_hours[i], FORMAT)
            out = datetime.strptime(work_hours[i + 1], FORMAT)
            hours += out - entry
        hours = hours.strftime("%H:%M:%S")
        return hours
    else:
        work_hours.pop()
        calculate_hours(work_hours)


def validadete_check(type_point: str, id_user: int) -> bool:

    last_check = read_checks_dada(id_user)
    if last_check:
        last_check = last_check[-1]
        if last_check["point_type"] == "Saida" and type_point == "Saida":
            return False
        elif last_check["point_type"] == "Entrada" and type_point == "Entrada":
            return False
        else:
            return True
    else:
        return True


def read_checks_dada(id_user):
    return [
        schemas.dump(user_date)
        for user_date in CheckIn.query.filter_by(user_id=id_user)
    ]
