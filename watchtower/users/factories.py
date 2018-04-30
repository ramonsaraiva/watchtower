import pendulum

from flask import current_app as app

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
        # user might have multiple fingerprints in future
        if user and user.fingerprints_user:
            return user.fingerprints[0]

        fingerprint = Fingerprint()
        fingerprint.user = user

        geo_data = app.config['GEOIP_READER'].city(args['ip'])
        # create geo data models

        fingerprint.created = pendulum.utcnow()
        return fingerprint
