import secrets

from ..devices.factories import UserAgentFactory
from ..users.factories import (
    FingerprintFactory,
    UserFactory,
)

from .models import (
    Event,
    Session,
)


class SessionFactory:

    @staticmethod
    def make(args):
        user = None
        if args['uid'] is not None:
            user = UserFactory.make(args['uid'])

        if args['sk'] is not None:
            session = Session.query.filter_by(key=args['sk']).first()
            if user and not session.fingerprint.has_ownership:
                session.fingerprint.assign_ownership(user)
            return session

        session = Session()
        session.key = args['sk'] or secrets.token_hex()

        session.fingerprint = FingerprintFactory.make(args, user)
        session.user_agent = UserAgentFactory.make(args['ua'])
        return session
