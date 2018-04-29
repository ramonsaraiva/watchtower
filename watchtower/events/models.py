from ..database import db


class Session(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(256))

    fingerprint_id = db.Column(db.Integer, db.ForeignKey('fingerprint.id'))
    fingerprint = db.relationship(
        'Fingerprint', backref=db.backref('sessions'))

    ip_address = db.Column(db.String(64))
    user_agent = db.Column(db.String(512))

    created = db.DateTime()


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    created = db.DateTime()
