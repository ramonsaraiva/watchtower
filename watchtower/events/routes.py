from flask import Blueprint
from flask_restful import Api

from .resources import EventResource


blueprint = Blueprint('events', __name__)
api = Api(blueprint)

api.add_resource(EventResource, '/event/')
