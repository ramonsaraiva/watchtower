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

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': f'{self.brand} {self.family} {self.model}',
            'version': f'{self.major} {self.minor} {self.patch} {self.patch_minor}'
        }


class UserAgent(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.String(512))

    device_id = db.Column(
        db.Integer,
        db.ForeignKey('component.id', ondelete='CASCADE'),
        nullable=False)
    device = db.relationship(
        'Component', backref=db.backref('ua_device'),
        foreign_keys=[device_id])

    os_id = db.Column(
        db.Integer,
        db.ForeignKey('component.id', ondelete='CASCADE'),
        nullable=False)
    os = db.relationship(
        'Component', backref=db.backref('ua_os'), foreign_keys=[os_id])

    ua_id = db.Column(
        db.Integer,
        db.ForeignKey('component.id', ondelete='CASCADE'),
        nullable=False)
    ua = db.relationship(
        'Component', backref=db.backref('ua_ua'), foreign_keys=[ua_id])

    def __repr__(self) -> str:
        return f'<UserAgent {self.os} {self.device} {self.ua}>'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'raw': self.raw,
            'device_id': self.device_id,
            'os_id': self.os_id,
            'ua_id': self.ua_id
        }
