import json

from django.http import JsonResponse

from backend import service


def property_metadata(request):
    if request.method == 'GET':
        result = service.get_all_property_metadata()
        return JsonResponse(result)
