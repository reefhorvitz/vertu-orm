import django_filters as df
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from backend.models import Appointment
from backend.schema.node import RegularIdNode


class AppointmentNode(DjangoObjectType):
    class Meta:
        model = Appointment
        interfaces = (RegularIdNode,)


class AppointmentFilter(df.FilterSet):
    customer_id = df.NumberFilter(field_name='customer__id')
    seller_id = df.NumberFilter(field_name='property__seller__id')

    class Meta:
        model = Appointment
        fields = ['customer_id', 'seller_id']


class Query:
    appointment = RegularIdNode.Field(AppointmentNode)
    all_appointments = DjangoFilterConnectionField(AppointmentNode, filterset_class=AppointmentFilter)
