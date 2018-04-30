from pathlib import Path


class Config:

    DEBUG = False
    TESTING = False

    BASE_DIR = Path().cwd()

    SQLALCHEMY_TRACK_MODIFICATIONS = False
