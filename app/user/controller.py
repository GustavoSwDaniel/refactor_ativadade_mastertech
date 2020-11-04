from flask import request, jsonify

from app.user import bp
from app.user import schemas as user_schemas
from app.user import service as user_services
from app.user.models import User

schema = user_schemas.UserSchema()


@bp.route("/cadastro", methods=["POST"])
def register_user():
    user = schema.load(request.json)
    validation_unique_cpf = user_services.find_exist_user_cpf(cpf=user.cpf)
    if validation_unique_cpf:
        try:
            user_object = user_services.save_user(user)
            return jsonify(schema.dump(user_object)), 201
        except Exception:
            return "Internal Error", 500

    return {"message": "CPF already registered"}, 404


@bp.route("/users", methods=["GET"])
def list_users():
    return jsonify([schema.dump(User) for User in User.query.all()]), 200


@bp.route("/user/<int:user_id>", methods=["GET"])
def find_user(user_id):
    user = user_services.find_user(user_id)
    if user:
        return jsonify(schema.dump(user)), 200
    return {"message": "User not Found"}, 404


@bp.route("/updade/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    up_user = request.json
    test = user_services.updade_user(user_id, up_user)
    if test:
        return "teste"
    return "bad"


@bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status_delete = user_services.delete_user(user_id)
    if status_delete:
        return {"message": "User successfully deleted"}, 200
    return {"message": "User not Found"}, 404
