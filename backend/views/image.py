from io import BytesIO

from django.http import JsonResponse
from rest_framework.views import APIView

from backend.service import image as service


class UploadImage(APIView):
    def post(self, request):
        image = request.FILES['file']
        result = {'url': service.upload_image(image)}
        return JsonResponse(result)
