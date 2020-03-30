from django.http import JsonResponse
from rest_framework import serializers, permissions, status
from rest_framework.views import APIView

from backend.serializers.user import UserSerializerWithToken
from backend.service import auth as service, Image

from backend.models import UserBase
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView


class UserBaseSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = UserBase
        exclude = ("password",)


def validate_login(request):
    if request.method == "GET":
        email = request.GET.get('email')
        token = request.GET.get('token')
        user = service.validate_login(email, token)
        user = UserBaseSerializer(user).data
        return JsonResponse(user)


# class UserList(APIView):
#     """
#     Create a new user. It's called 'UserList' because normally we'd have a get
#     method here too, for retrieving a list of all User objects.
#     """
#
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter
