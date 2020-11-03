from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    config.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.user import bp as user_bp

    app.register_blueprint(user_bp)

    return app
