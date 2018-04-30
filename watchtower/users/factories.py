import pendulum

from .models import (
    Fingerprint,
    User,
)


class UserFactory:

    @staticmethod
    def make(identifier):
        user = User.query.filter_by(identifier=identifier).first()
        if user is not None:
            return user

        user = User()
        user.identifier = identifier
        user.created = pendulum.utcnow()
        return user


class FingerprintFactory:

    @staticmethod
    def make(args, user=None):
        # temporary fake fingerprint
        fingerprint = Fingerprint()
        fingerprint.user = user
        fingerprint.created = pendulum.utcnow()
        return fingerprint
