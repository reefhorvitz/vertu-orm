from django.db import models

from backend.models.property import Property
from backend.models.user import User


class Appointment(models.Model):
    customer = models.ForeignKey(User, related_name="appointments_as_customer", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    time = models.DateTimeField('Time of the appointment')
    is_completed = models.BooleanField('Is the meeting happened')
    session_id = models.CharField('opentok sessionId', max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.customer.first_name} appointment about property {self.property.id}'
