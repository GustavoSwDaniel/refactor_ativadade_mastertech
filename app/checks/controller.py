from flask import request, jsonify


from app.checks import bp
from app.checks import schemas as check_schemas
from app.checks import service as check_services
from app.checks.models import CheckIn

schema = check_schemas.CheckSchema()


@bp.route("/point/<int:user_id>", methods=["POST"])
def check_point(user_id):

    check = schema.load(request.json)
    check_user = schema.dump(check)
    check_user["tipo_da_batida"]
    validate = check_services.validadete_entrada(
        check_user["tipo_da_batida"],
        user_id,
    )
    if validate:
        check = check_services.register_check_User(user_id, check)
        if check:
            return jsonify(schema.dump(check)), 201
        return {"message": "User not found"}, 404
    return {"message": "<Tipo de Entrada> repeated"}, 400


@bp.route("/checks/<int:user_id>", methods=["GET"])
def list_checks(user_id):
    check_hours = check_services.worked_hour(user_id)
    if check_hours:
        return jsonify(
            {"Total de Horas trabalhadas": check_hours},
            [
                schema.dump(check)
                for check in CheckIn.query.filter_by(user_id=user_id).all()
            ],
        )
    return {"message": "User not found"}, 404
