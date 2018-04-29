import os

from flask import Flask

from .database import db
from .users.models import *
from .events.models import *

def create_app():
    app = Flask(__name__)
    environment = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(f'watchtower.config.{environment}.Config')
    db.init_app(app)
    return app


app = create_app()


@app.cli.command()
def create_db():
    db.create_all()


@app.cli.command()
def drop_db():
    db.drop_all()
