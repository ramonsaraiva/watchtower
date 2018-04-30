from ua_parser import user_agent_parser

from .models import (
    Component,
    UserAgent,
)


class ComponentFactory:

    @staticmethod
    def make(data) -> Component:
        component = Component.query.filter_by(**data).first()
        if component is not None:
            return component

        return Component(
            brand=data.get('brand', None),
            family=data.get('family', None),
            model=data.get('model', None),
            major=data.get('major', None),
            minor=data.get('minor', None),
            patch=data.get('patch', None),
            patch_minor=data.get('patch_minor', None))


class UserAgentFactory:

    @staticmethod
    def make(raw) -> UserAgent:
        user_agent = UserAgent.query.filter_by(raw=raw).first()
        if user_agent is not None:
            return user_agent

        ua_data = user_agent_parser.Parse(raw)
        return UserAgent(
            raw=raw,
            device=ComponentFactory.make(ua_data['device']),
            os=ComponentFactory.make(ua_data['os']),
            ua=ComponentFactory.make(ua_data['user_agent']))
