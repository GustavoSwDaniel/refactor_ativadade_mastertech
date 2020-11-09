from flask import request

from app.checks import bp
from app.checks import schemas as check_schemas
from app.checks import service as check_services

schema = check_schemas.CheckSchema()


@bp.route("/point/<int:user_id>", methods=["POST"])
def check_point(user_id):
    check = schema.load(request.json)
    confirmation = check_services.register_check_User(user_id, check)
    return confirmation


@bp.route("/point/<int:user_id>", methods=["GET"])
def list_checks(user_id):
    check_hours = check_services.worked_hour(user_id)
    return check_hours


#