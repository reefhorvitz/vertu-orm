import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models.property_metadata import Facility, OtherData, Heating, Cooling, Amenity, Parking, Tag, Type
from backend.schema.node import RegularIdNode


class FacilityNode(DjangoObjectType):
    class Meta:
        model = Facility
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class OtherDataNode(DjangoObjectType):
    class Meta:
        model = OtherData
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class HeatingNode(DjangoObjectType):
    class Meta:
        model = Heating
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class AmenityNode(DjangoObjectType):
    class Meta:
        model = Amenity
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class ParkingNode(DjangoObjectType):
    class Meta:
        model = Parking
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class CoolingNode(DjangoObjectType):
    class Meta:
        model = Cooling
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class TypeNode(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (RegularIdNode,)
        filter_fields = ['name']


class Query:
    type = RegularIdNode.Field(TypeNode)
    all_types = DjangoFilterConnectionField(TypeNode)
    tag = RegularIdNode.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TypeNode)
    cooling = RegularIdNode.Field(CoolingNode)
    all_coolings = DjangoFilterConnectionField(CoolingNode)
    heating = RegularIdNode.Field(HeatingNode)
    all_heatings = DjangoFilterConnectionField(HeatingNode)
    facility = RegularIdNode.Field(FacilityNode)
    all_facilities = DjangoFilterConnectionField(FacilityNode)
    amenity = RegularIdNode.Field(AmenityNode)
    all_amenities = DjangoFilterConnectionField(AmenityNode)
    other_date = RegularIdNode.Field(OtherDataNode)
    all_other_data = DjangoFilterConnectionField(OtherDataNode)
    parking = RegularIdNode.Field(ParkingNode)
    all_parkings = DjangoFilterConnectionField(ParkingNode)

