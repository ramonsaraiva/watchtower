from ..database import db


class Component(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(64))
    family = db.Column(db.String(64))
    model = db.Column(db.String(64))

    major = db.Column(db.String(16))
    minor = db.Column(db.String(16))
    patch = db.Column(db.String(16))
    patch_minor = db.Column(db.String(16))

    def __repr__(self) -> str:
        return f'<Component {self.brand} {self.family} {self.model}>'


class UserAgent(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.String(512))

    device_id = db.Column(db.Integer, db.ForeignKey('component.id'))
    device = db.relationship('Component', backref=db.backref('ua_devices'))

    os_id = db.Column(db.Integer, db.ForeignKey('component.id'))
    os = db.relationship('Component', backref=db.backref('ua_oss'))

    ua_id = db.Column(db.Integer, db.ForeignKey('component.id'))
    ua = db.relationship('Component', backref=db.backref('ua_uas'))

    def __repr__(self) -> str:
        return f'<UserAgent {self.os} {self.device} {self.ua}>'
