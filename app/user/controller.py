from flask import request, jsonify

from app.user import bp
from app.user import schemas as user_schemas
from app.user import service as user_services


@bp.route("/cadastro", methods=["POST"])
def register_user():
    schema = user_schemas.UserRegisterSchema()
    user = schema.load(request.json)
    user_object = user_services.save_user(user)
    return jsonify(schema.dump(user_object)), 201


@bp.route("/users", methods=["GET"])
def list_users():
    user_list = user_services.show_user()
    print(user_list)


@bp.route("/user/<int:user_id>", methods=["GET"])
def find_user(user_id):
    ...


@bp.route("/updade/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    ...


@bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    ...
