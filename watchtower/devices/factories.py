from ua_parser import user_agent_parser

from ..database import db

from .models import (
    Component,
    UserAgent,
)


class ComponentFactory:

    @staticmethod
    def make(data):
        component = Component.query.filter_by(**data).first()
        if component is not None:
            return component

        component = Component()
        component.brand = data.get('brand', None)
        component.family = data.get('family', None)
        component.model = data.get('model', None)
        component.major = data.get('major', None)
        component.minor = data.get('minor', None)
        component.patch = data.get('patch', None)
        component.patch_minor = data.get('patch_minor', None)
        return component


class UserAgentFactory:

    @staticmethod
    def make(raw):
        user_agent = UserAgent.query.filter_by(raw=raw).first()
        if user_agent is not None:
            return user_agent

        user_agent = UserAgent()
        user_agent.raw = raw

        ua_data = user_agent_parser.Parse(raw)
        user_agent.device = ComponentFactory.make(ua_data['device'])
        user_agent.os = ComponentFactory.make(ua_data['os'])
        user_agent.ua = ComponentFactory.make(ua_data['user_agent'])

        return user_agent
