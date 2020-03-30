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
    id = df.BaseInFilter(field_name="pk")
    country = df.CharFilter(field_name='location__city__country__name')
    city = df.CharFilter(field_name='location__city__name')
    city_id = df.NumberFilter(field_name='location__city__pk')
    amenities = df.BaseInFilter(field_name='amenities__name')
    facilities = df.BaseInFilter(field_name='facilities__name')
    tags = df.BaseInFilter(field_name='tags__name')
    max_price = df.NumberFilter(field_name='price', lookup_expr='lte')
    min_price = df.NumberFilter(field_name='price', lookup_expr='gte')
    bedroom_number = df.NumberFilter(field_name='bedroom_number', lookup_expr='gte')
    bathroom_number = df.NumberFilter(field_name='bathroom_number', lookup_expr='gte')
    seller_id = df.NumberFilter(field_name='seller__id')

    class Meta:
        model = Property
        fields = ['id', 'bedroom_number', 'country', 'city', 'city_id', 'bathroom_number', 'amenities', 'facilities',
                  'tags', 'max_price', 'min_price', 'seller_id']


class Query:
    property = RegularIdNode.Field(PropertyNode)
    all_properties = DjangoFilterConnectionField(PropertyNode, filterset_class=PropertyFilter)
