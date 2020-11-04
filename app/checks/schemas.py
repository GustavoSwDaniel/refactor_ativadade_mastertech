from marshmallow import Schema, fields, validate, post_load
from app.checks.models import CheckIn


class CheckSchema(Schema):
    id_pont = fields.Integer(data_key="id_point")
    usuario_responsavel = fields.String(
        validate=validate.Length(max=255),
        required=True,
        data_key="usario_responsavel",
    )

    tipo_da_batida = fields.String(required=True)
    data_hora_batida = fields.DateTime()
    user_id = fields.Integer()

    @post_load
    def make_check(self, check, **kwargs):
        return CheckIn(**check)
