from flask import request, jsonify

from app.user import bp
from app.user import schemas as user_schemas
from app.user import service as user_services
from app.user.models import User

schema = user_schemas.UserSchema()


@bp.route("/cadastro", methods=["POST"])
def register_user():
    user = schema.load(request.json)
    user_object = user_services.save_user(user)
    return jsonify(schema.dump(user_object)), 201


@bp.route("/users", methods=["GET"])
def list_users():
    return jsonify([schema.dump(User) for User in User.query.all()]), 200


@bp.route("/user/<int:user_id>", methods=["GET"])
def find_user(user_id):
    return jsonify(schema.dump(user_services.find_user(user_id)))


@bp.route("/updade/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    ...


@bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    ...
