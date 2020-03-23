from django.http import JsonResponse

from backend.service import opentok as service


def opentok(request, appointment_id):
    if request.method == 'GET':
        session_id, token = service.generate_token(appointment_id)
        result = {
            'sessionId': session_id,
            'token': token
        }
        return JsonResponse(result)
