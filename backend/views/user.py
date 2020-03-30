import json

from django.http import JsonResponse

from backend.service import user as service
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from backend.views.auth import UserBaseSerializer


def User(request, user_id):
    body = json.loads(request.body)
    name = body['name']
    email = body['email']
    phone = body['phone']
    user = service.edit_user_details(user_id, name, phone, email)
    return JsonResponse(UserBaseSerializer(user).data)
