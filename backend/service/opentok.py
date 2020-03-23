from opentok import OpenTok

from backend.models import Appointment

api_key = '46598552'
secret = '7e8e26cdd3d9fac7bcb5df1a6d9c06db34adc199'
opentok = OpenTok(api_key, secret)


def create_session():
    session = opentok.create_session()
    return session.session_id


def generate_token(appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    session_id = appointment.session_id
    if not session_id:
        session_id = create_session()
        appointment.session_id = session_id
        appointment.save()
    token = opentok.generate_token(session_id)
    return session_id, token
