import graphene
import backend.schema
from graphene_django.debug import DjangoDebug


class Query(backend.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query)
