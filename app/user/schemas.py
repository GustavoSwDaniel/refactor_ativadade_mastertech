from marshmallow import Schema, fields, validate


class UserRegisterSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome_completo = fields.String(
        validate=validate.Length(max=255),
        load_only=True,
        required=True,
        data_key="nome_compelto",
    )
    cpf = fields.String(
        validate=validate.Length(11),
        required=True,
        data_key="password",
    )
    email = fields.Email(
        required=True,
        load_only=True,
    )
    data_de_cadastro = fields.Date(
        required=True,
    )


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
