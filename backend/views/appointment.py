import json

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.models import Appointment
from backend.service import appointment as service
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class Appointments(APIView):
    def post(self, request):
        body = json.loads(request.body)
        time = body['time']
        user_id = body['userId']
        property_id = body['propertyId']
        appointment = service.create_appointment(time, property_id, user_id)
        return JsonResponse(AppointmentSerializer(appointment).data)
