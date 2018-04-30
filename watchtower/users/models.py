from ..database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True)

    created = db.DateTime(db.DateTime)

    def __repr__(self) -> str:
        return f'<User {self.identifier}>'

    def serialize(self):
        return {
            'identifier': self.identifier,
            'fingerprints': [f.serialize() for f in self.fingerprints_user]
        }


class Fingerprint(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship(
        'User', backref=db.backref('fingerprints_user'))

    location_id = db.Column(
        db.Integer, db.ForeignKey('location.id', ondelete='CASCADE'))
    location = db.relationship(
        'Location', backref=db.backref('fingerprints_location'))

    created = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f'<Fingerprint {self.id}>'

    @property
    def has_ownership(self) -> bool:
        return bool(self.user_id)

    def assign_ownership(self, user) -> None:
        self.user = user

    def serialize(self) -> dict:
        return {
            'location': self.location.serialize() if self.location else None,
            'sessions': [s.serialize() for s in self.sessions_fingerprint]
        }
