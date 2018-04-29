from .base import Config as BaseConfig


class Config(BaseConfig):

    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BaseConfig.BASE_DIR.joinpath('db.sqlite')}"
