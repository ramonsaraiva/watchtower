from flask import current_app as app
from flask_restful import (
    reqparse,
    Resource,
)

from ..events.factories import (
    EventFactory,
    SessionFactory,
)
from ..users.models import *
from ..devices.models import *
from ..events.models import *


class EventResource(Resource):

    def parser(self):
        """
        Parses an event.

        # sk    Session key
        # uid   User identificator
        # ts    Timestamp
        # ua    User Agent
        # ec    Event category
        # en    Event name
        # ed    Event data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('sk', type=str)
        parser.add_argument('uid', type=str)
        parser.add_argument('ts', type=str, required=True)
        parser.add_argument('ua', type=str, required=True)
        parser.add_argument('ip', type=str, required=True)
        parser.add_argument('ec', type=str, required=True)
        parser.add_argument('en', type=str, required=True)
        parser.add_argument('ed', type=dict)
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
            event = EventFactory.make(session, args)

            db.session.add(session)
            db.session.commit()

        return {'key': session.key}
