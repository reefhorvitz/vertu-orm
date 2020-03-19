from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
