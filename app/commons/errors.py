from flask import jsonify
from werkzeug.exceptions import HTTPException


class BasicError(Exception):
    def __init__(self, message):
        self.message = message


class DublicateUserError(BasicError):
    def __init__(
        self,
        code_status=422,
        massage="The user is already registered",
    ):
        super().__init__(massage)
        self.code_status = code_status


class UserDoesNotExistError(BasicError):
    def __init__(self, message="User does not exist"):
        super().__init__(message)
