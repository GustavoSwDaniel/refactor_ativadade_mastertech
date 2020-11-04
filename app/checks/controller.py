from flask import request, jsonify


from app.checks import bp
from app.checks import schemas as check_schemas
from app.checks import service as check_services
from app.checks.models import CheckIn

schema = check_schemas.CheckSchema()


@bp.route("/point/<int:user_id>", methods=["POST"])
def check_point(user_id):
    try:
        check = schema.load(request.json)
        check = check_services.register_check_User(user_id, check)
        if check:
            return jsonify(schema.dump(check)), 201
        return {"message": "User not found"}, 404
    except Exception:
        return {"message": "error"}, 404


@bp.route("/checks/<int:user_id>", methods=["GET"])
def list_checks(user_id):
    return jsonify(
        [
            schema.dump(check)
            for check in CheckIn.query.filter_by(user_id=user_id).all()
        ],
    )
