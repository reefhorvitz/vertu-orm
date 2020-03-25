from django.http import JsonResponse
from rest_framework import serializers
from backend.service import auth as service

from backend.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


def validate_login(request):
    if request.method == "GET":
        email = request.GET.get('email')
        token = request.GET.get('token')
        service.validate_login(email, token)
