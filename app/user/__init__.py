from flask import Blueprint
from app.user import models

bp = Blueprint("user", __name__)

from app.user import controller
