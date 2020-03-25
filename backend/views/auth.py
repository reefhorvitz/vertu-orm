from django.http import JsonResponse
from rest_framework import serializers
from backend.service import auth as service, Image

from backend.models import UserBase


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = UserBase
        exclude = ('password',)


def validate_login(request):
    if request.method == "GET":
        email = request.GET.get('email')
        token = request.GET.get('token')
        user = service.validate_login(email, token)
        user = UserSerializer(user).data
        return JsonResponse(user)
