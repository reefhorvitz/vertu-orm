import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models import Appointment
from backend.schema.node import RegularIdNode


class AppointmentNode(DjangoObjectType):
    class Meta:
        model = Appointment
        interfaces = (RegularIdNode,)
        filter_fields = ['customer__id', 'seller__id']


class Query:
    appointment = RegularIdNode.Field(AppointmentNode)
    all_appointments = DjangoFilterConnectionField(AppointmentNode)
