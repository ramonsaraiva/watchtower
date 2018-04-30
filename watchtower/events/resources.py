from flask_restful import Resource


class EventResource(Resource):

    def get(self):
        return {'hi': 'hi'}
