from flask_restful import (
    reqparse,
    Resource,
)


class EventResource(Resource):

    # used as reference
    PARAMETERS = {
        'sk': 'session key (secrets.token_hex())',
        'uid': 'user identifier',
        'ts': 'timestamp',
        'ua': 'user agent',
        'ip': 'ip address',
        'dh': 'document hostname',
        'dp': 'page path',
        'dt': 'page title',
        'ec': 'event category',
        'en': 'event name',
        'ed': 'event data',
    }

    def parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sk', type=str, required=False)
        parser.add_argument('uid', type=str, required=False)
        parser.add_argument('ts', type=str, required=False)
        return parser

    def post(self):
        parser = self.parser()
        args = parser.parse_args()
