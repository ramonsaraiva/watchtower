from flask_restful import (
    reqparse,
    Resource,
)

from ..events.factories import (
    EventFactory,
    SessionFactory,
)


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
        from users.models import User, Fingerprint
        users = User.query.all()
        fingerprints = Fingerprint.query.filter_by(user=None)

        return {
            'users': [u.serialize() for u in users],
            'fingerprints': [f.serialize() for f in fingerprints]
        }

    def post(self):
        parser = self.parser()
        args = parser.parse_args()

        with db.session.no_autoflush:
            session = SessionFactory.make(args)
            EventFactory.make(session, args)

            db.session.add(session)
            db.session.commit()

        return {'key': session.key}
