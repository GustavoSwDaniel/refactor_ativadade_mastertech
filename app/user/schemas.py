from marshmallow import Schema, fields, validate, post_load

from app.user.models import User
from app.helpers.validade import ValidateCPF


class UserSchema(Schema):

    id = fields.Integer(data_key="id", dump_only=True)
    full_name = fields.String(
        validate=validate.Length(max=255),
        required=True,
        data_key="full_name",
    )
    cpf = fields.String(
        validate=ValidateCPF,
    )
    email = fields.Email(
        required=True,
        data_key="email",
    )
    registration_date = fields.Date(dump_only=True)

    @post_load
    def make_user(self, user, **kwargs):
        return User(**user)


class UpdateUserSchema(Schema):
    full_name = fields.String(
        validate=validate.Length(max=255),
        data_key="full_name",
    )

    cpf = fields.String(
        validate=validate.Length(11),
        data_key="cpf",
    )
    email = fields.Email(
        data_key="email",
    )
