from geoip2.errors import GeoIP2Error
import pendulum

from flask import current_app as app

from ..geo.factories import LocationFactory
from .models import (
    Fingerprint,
    User,
)


class UserFactory:

    @staticmethod
    def make(identifier) -> User:
        user = User.query.filter_by(identifier=identifier).first()
        if user is not None:
            return user

        user = User()
        user.identifier = identifier
        user.created = pendulum.utcnow()
        return user


class FingerprintFactory:

    @staticmethod
    def make(args, user=None) -> Fingerprint:
        # user might have multiple fingerprints in future
        if user and user.fingerprints_user:
            return user.fingerprints_user[0]

        fingerprint = Fingerprint()
        fingerprint.user = user

        try:
            geo_data = app.config['GEOIP_READER'].city(args['ip'])
            fingerprint.location = LocationFactory.make(geo_data)
        except GeoIP2Error:
            app.logger.warning(
                f'Geo data could not be retrieved for {args["ip"]}')

        fingerprint.created = pendulum.utcnow()
        return fingerprint
