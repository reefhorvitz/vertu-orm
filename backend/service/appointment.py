from backend.models import Appointment


def create_appointment(time, property_id, user_id):
    appointment = Appointment.objects.create(customer_id=user_id, property_id=property_id, time=time)
    return appointment
