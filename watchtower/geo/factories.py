from .models import (
    City,
    Country,
    Location,
    State,
)


class CountryFactory:

    @staticmethod
    def make(geo_data) -> Country:
        country = Country.query.filter_by(name=geo_data.country.name).first()
        if country is not None:
            return country
        return Country(
            name=geo_data.country.name, code=geo_data.country.iso_code)


class StateFactory:

    @staticmethod
    def make(geo_data) -> State:
        state_data = geo_data.subdivisions.most_specific
        state = State.query.filter_by(name=state_data.name).first()
        if state is not None:
            return state

        return State(
            name=state_data.name,
            code=state_data.iso_code,
            country=CountryFactory.make(geo_data))


class CityFactory:

    @staticmethod
    def make(geo_data) -> City:
        city = City.query.filter_by(name=geo_data.city.name).first()
        if city is not None:
            return city

        return City(
            name=geo_data.city.name,
            state=StateFactory.make(geo_data))


class LocationFactory:

    @staticmethod
    def make(geo_data) -> Location:
        return Location(
            city=CityFactory.make(geo_data),
            postal_code=geo_data.postal.code,
            latitude=geo_data.location.latitude,
            longitude=geo_data.location.longitude)
