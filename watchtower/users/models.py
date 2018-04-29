from ..database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True)

    created = db.DateTime()


class Fingerprint(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('fingerprints'))

    created = db.DateTime()
