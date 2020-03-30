import json

from django.http import JsonResponse
from rest_framework.views import APIView

from backend import service


class PropertyMetadata(APIView):
    def get(self, request):
        result = service.get_all_property_metadata()
        return JsonResponse(result)
