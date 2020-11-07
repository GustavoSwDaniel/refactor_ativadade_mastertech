from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.user import bp as user_bp

    app.register_blueprint(user_bp)

    from app.checks import bp as check_bp

    app.register_blueprint(check_bp)

    from app.commons import bp as common_bp

    app.register_blueprint(common_bp)

    return app
