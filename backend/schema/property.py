import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models import Property
from backend.schema.node import RegularIdNode


class PropertyNode(DjangoObjectType):
    class Meta:
        model = Property
        interfaces = (RegularIdNode,)


class PropertyFilter(df.FilterSet):
    country = df.CharFilter(field_name='location__city__country__name')
    city = df.CharFilter(field_name='location__city__name')
    amenities = df.BaseInFilter(field_name='amenities__name')
    facilities = df.BaseInFilter(field_name='facilities__name')
    tags = df.BaseInFilter(field_name='tags__name')

    class Meta:
        model = Property
        fields = ['bedroom_number', 'country', 'city', 'bathroom_number', 'amenities', 'facilities', 'tags']


class Query:
    property = RegularIdNode.Field(PropertyNode)
    all_properties = DjangoFilterConnectionField(PropertyNode, filterset_class=PropertyFilter)
