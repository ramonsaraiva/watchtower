from  ..database import db


class Country(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    code = db.Column(db.String(4))

    def __repr__(self) -> str:
        return f'<Country {self.code} {self.name}>'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code
        }


class State(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    country_id = db.Column(
        db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'))
    country = db.relationship(
        'Country', backref=db.backref('states'))

    name = db.Column(db.String(32))
    code = db.Column(db.String(4))

    def __repr__(self) -> str:
        return f'<State {self.code} {self.name}>'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'country': self.country.serialize()
        }


class City(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    state_id = db.Column(
        db.Integer, db.ForeignKey('state.id', ondelete='CASCADE'))
    state = db.relationship(
        'State', backref=db.backref('cities'))

    name = db.Column(db.String(32))

    def __repr__(self) -> str:
        return f'<City {self.name}>'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state.serialize()
        }


class Location(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    city_id = db.Column(
        db.Integer, db.ForeignKey('city.id', ondelete='CASCADE'))
    city = db.relationship(
        'City', backref=db.backref('locations'))

    postal_code = db.Column(db.String(32))
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))

    def __repr__(self) -> str:
        return f'<Location {self.latitude} {self.longitude}>'

    def serialize(self) -> dict:
        return {
            'city': self.city.serialize(),
            'postal_code': self.postal_code,
            'latitude': float(self.latitude),
            'longitude': float(self.longitude)
        }
