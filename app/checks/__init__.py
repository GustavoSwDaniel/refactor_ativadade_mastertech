from flask import Blueprint
from app.checks import models

bp = Blueprint("checks", __name__)

from app.checks import controller
