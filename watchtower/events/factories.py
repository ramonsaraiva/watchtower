import pendulum
import secrets

from ..devices.factories import UserAgentFactory
from ..users.factories import (
    FingerprintFactory,
    UserFactory,
)

from .models import (
    Event,
    EventCategory,
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
            if session:
                if user and not session.fingerprint.has_ownership:
                    session.fingerprint.assign_ownership(user)
                return session

        utcnow = pendulum.utcnow()
        expiration = utcnow.add(days=1)
        return Session(
            key=args['sk'] or secrets.token_hex(),
            fingerprint=FingerprintFactory.make(args, user),
            user_agent=UserAgentFactory.make(args['ua']),
            created=utcnow,
            expiration=expiration)


class EventCategoryFactory:

    @staticmethod
    def make(name):
        category = EventCategory.query.filter_by(name=name).first()
        if category is not None:
            return category
        return EventCategory(name=name, created=pendulum.utcnow())


class EventFactory:

    @staticmethod
    def make(session, args):
        category = EventCategoryFactory.make(args['ec'])
        return Event(
            category=category,
            session=session,
            name=args['en'],
            data=args['ed'],
            created=pendulum.utcnow())
