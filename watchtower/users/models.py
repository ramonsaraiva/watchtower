from ..database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True)

    created = db.DateTime(db.DateTime)

    def __repr__(self) -> str:
        return f'<User {self.identifier}>'


class Fingerprint(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('fingerprints', ondelete='SET NULL'))

    created = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f'<Fingerprint {self.id}>'
