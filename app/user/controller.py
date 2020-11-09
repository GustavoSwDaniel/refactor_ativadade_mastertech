from flask import request, jsonify
from werkzeug.exceptions import abort


from app.user import bp
from app.user import schemas as user_schemas
from app.user import service as user_services
from app.user.models import User

schema = user_schemas.UserSchema()


@bp.route("/user", methods=["POST"])
def register_user():

    user = schema.load(request.json)
    if user_services.find_exist_user_cpf(cpf=user.cpf):
        abort(400, "CPF already in use!")

    services = user_services.register_user(user)
    return services


@bp.route("/users", methods=["GET"])
def list_users():
    return jsonify([schema.dump(User) for User in User.query.all()]), 200


@bp.route("/user/<int:user_id>", methods=["GET"])
def find_user(user_id):

    user = user_services.find_user(user_id)
    return user


@bp.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    scheme_update = user_schemas.UpdateUserSchema()
    update = scheme_update.load(request.json)

    confirmation = user_services.updade_user(user_id, update)
    return confirmation


@bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status_delete = user_services.delete_user(user_id)
    return status_delete
