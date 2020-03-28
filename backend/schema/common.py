import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from backend.models import Country, City, Location, Image
from backend.schema.node import RegularIdNode


class CountryNode(DjangoObjectType):
    class Meta:
        model = Country
        interfaces = (RegularIdNode,)


class CountryFilter(df.FilterSet):
    name = df.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Country
        fields = ['name']


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        interfaces = (RegularIdNode,)
        filter_fields = ['name', 'country__name']


class CityFilter(df.FilterSet):
    name = df.CharFilter(lookup_expr='icontains')
    country_name = df.CharFilter(field_name='country__name', lookup_expr='icontains')

    class Meta:
        model = City
        fields = ['name', 'country_name']


class LocationNode(DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (RegularIdNode,)
        filter_fields = ['city__name', 'city__country__name']


class LocationFilter(df.FilterSet):
    country_name = df.CharFilter(field_name='city__country__name', lookup_expr='icontains')
    city_name = df.CharFilter(field_name='city__name', lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ['country_name', 'city_name']


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image


class Query:
    country = RegularIdNode.Field(CountryNode)
    city = RegularIdNode.Field(CityNode)
    location = RegularIdNode.Field(LocationNode)
    all_countries = DjangoFilterConnectionField(CountryNode, filterset_class=CountryFilter)
    all_cities = DjangoFilterConnectionField(CityNode, filterset_class=CityFilter)
    all_locations = DjangoFilterConnectionField(LocationNode, filterset_class=LocationFilter)
    image = RegularIdNode.Field(ImageNode)
