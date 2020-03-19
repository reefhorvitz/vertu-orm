import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models import User
from backend.schema.node import RegularIdNode


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (RegularIdNode,)
        fields = ['email', 'first_name', 'last_name']
        filter_fields = fields


class Query:
    user = RegularIdNode.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
