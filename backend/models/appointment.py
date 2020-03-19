from django.db import models

from backend.models.property import Property
from backend.models.user import User


class Appointment(models.Model):
    customer = models.ForeignKey(User, related_name="appointments_as_customer", on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name="appointments_as_seller", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    time = models.DateTimeField('Time of the appointment')
    is_completed = models.BooleanField('Is the meeting happened')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
