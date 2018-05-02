import geoip2.database

from .base import Config as BaseConfig


class Config(BaseConfig):

    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = f'postgresql://watchtower:watchtower@db:5432/watchtower'

    GEOIP_READER = geoip2.database.Reader(BaseConfig.BASE_DIR.joinpath('geo.mmdb'))
