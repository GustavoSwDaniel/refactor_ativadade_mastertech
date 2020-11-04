from marshmallow import Schema, fields, validate, post_load

from app.user.models import User


class UserSchema(Schema):

    id_user = fields.Integer(data_key="id", dump_only=True)
    nome_completo = fields.String(
        validate=validate.Length(max=255),
        required=True,
        data_key="nome_completo",
    )
    cpf = fields.String(
        validate=validate.Length(11),
        required=True,
        data_key="cpf",
    )
    email = fields.Email(
        required=True,
        data_key="email",
    )
    data_de_cadastro = fields.Date(dump_only=True)

    @post_load
    def make_user(self, user, **kwargs):
        return User(**user)


class CheckInSchema(Schema):
    id_point = fields.Integer(dump_only=True)
    usuario_responsavel = fields.String(
        validate=validate.Length(max=255), required=True
    )
    tipo_da_batida = fields.String(required=True)
    data_hora_batida = fields.DateTime(
        required=True,
    )
    id_user = fields.Integer(required=True)
