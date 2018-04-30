from ..database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True)

    created = db.DateTime(db.DateTime)

    def __repr__(self) -> str:
        return f'<User {self.identifier}>'

    def serialize(self):
        return {
            'id': self.id,
            'identifier': self.identifier
        }


class Fingerprint(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship(
        'User', backref=db.backref('fingerprints'))

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
            'id': self.id,
            'user_id': self.user_id,
        }
