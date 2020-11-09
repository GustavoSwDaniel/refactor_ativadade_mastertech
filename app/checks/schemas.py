from marshmallow import Schema, fields, validate, post_load
from app.checks.models import CheckIn


class CheckSchema(Schema):
    id_pont = fields.Integer(data_key="id_point")
    responsible_user = fields.String(
        validate=validate.Length(max=255),
        required=True,
        data_key="responsible_user",
    )

    point_type = fields.String(required=True)
    point_date_time = fields.DateTime()
    user_id = fields.Integer()

    @post_load
    def make_check(self, check, **kwargs):
        return CheckIn(**check)
