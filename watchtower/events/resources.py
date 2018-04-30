from flask import current_app as app
from flask_restful import (
    reqparse,
    Resource,
)

from ..events.factories import SessionFactory
from ..users.models import *
from ..devices.models import *
from ..events.models import *


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
        parser.add_argument('ua', type=str, required=True)
        return parser

    def get(self):
        """Temporary visualizer."""
        users = User.query.all()
        fingerprints = Fingerprint.query.all()
        sessions = Session.query.all()
        events = Event.query.all()
        uas = UserAgent.query.all()
        components = Component.query.all()

        return {
            'users': [user.serialize() for user in users],
            'fingerprints': [fp.serialize() for fp in fingerprints],
            'sessions': [s.serialize() for s in sessions],
            'events': [e.serialize() for e in events],
            'uas': [ua.serialize() for ua in uas],
            'components': [c.serialize() for c in components]
        }

    def post(self):
        parser = self.parser()
        args = parser.parse_args()

        with db.session.no_autoflush:
            session = SessionFactory.make(args)
            db.session.add(session)
            db.session.commit()

        return {'success': True}
