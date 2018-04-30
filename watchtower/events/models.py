from ..database import db


class Session(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64))

    fingerprint_id = db.Column(
        db.Integer,
        db.ForeignKey('fingerprint.id', ondelete='CASCADE'),
        nullable=False)
    fingerprint = db.relationship(
        'Fingerprint', backref=db.backref('sessions_fingerprint'))

    user_agent_id = db.Column(
        db.Integer,
        db.ForeignKey('user_agent.id', ondelete='CASCADE'),
        nullable=False)
    user_agent = db.relationship(
        'UserAgent', backref=db.backref('sessions_ua'))

    ip_address = db.Column(db.String(64))

    created = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f'<Session {self.key}>'

    def serialize(self) -> dict:
        return {
            'key': self.key,
            'user_agent': self.user_agent.serialize(),
            'events': [e.serialize() for e in self.events_session]
        }


class EventCategory(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self) -> str:
        return f'<EventCategory {self.name}>'

    def serialize(self) -> dict:
        return {
            'name': self.name
        }


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    data = db.Column(db.JSON)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('event_category.id', ondelete='CASCADE'),
        nullable=False)
    category = db.relationship(
        'EventCategory', backref=db.backref('events_category'))

    session_id = db.Column(
        db.Integer,
        db.ForeignKey('session.id', ondelete='CASCADE'),
        nullable=False)
    session = db.relationship(
        'Session', backref=db.backref('events_session'))

    created = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f'<Event {self.name}>'

    def serialize(self) -> dict:
        return {
            'category': self.category.name,
            'name': self.name,
            'data': self.data,
        }
