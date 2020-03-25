import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models import UserBase, Agent
from backend.schema.node import RegularIdNode

fields = ['email', 'name', 'image', 'phone']


class UserBaseNode(DjangoObjectType):
    class Meta:
        model = UserBase
        interfaces = (RegularIdNode,)
        fields = fields
        filter_fields = fields


class AgentNode(DjangoObjectType):
    class Meta:
        model = Agent
        fields = fields


class Query:
    user = RegularIdNode.Field(UserBaseNode)
    all_users = DjangoFilterConnectionField(UserBaseNode)
    agent = RegularIdNode.Field(AgentNode)
