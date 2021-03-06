"""class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/banco.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test_banco.db"


app_config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
}"""
