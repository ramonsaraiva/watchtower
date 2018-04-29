import os

from flask import Flask

from .database import db


def create_app():
    app = Flask(__name__)
    environment = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(f'watchtower.config.{environment}.Config')
    db.init_app(app)
    return app


app = create_app()
