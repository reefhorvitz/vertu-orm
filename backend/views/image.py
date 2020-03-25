from io import BytesIO

from django.http import JsonResponse

from backend.service import image as service


def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['file']
        result = {'url': service.upload_image(image)}
        return JsonResponse(result)
