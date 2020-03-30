from django.http import JsonResponse
from rest_framework.views import APIView

from backend.service import opentok as service


class OpenTok(APIView):
    def get(self, request, appointment_id):
        api_key, session_id, token = service.generate_token(appointment_id)
        result = {
            'apiKey': api_key,
            'sessionId': session_id,
            'token': token
        }
        return JsonResponse(result)
