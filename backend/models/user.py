from django.db import models
from backend.models.common import Image
from backend.models.property_metadata import Tag


class UserBase(models.Model):
    email = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=100)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Agent(UserBase):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'AGENT'
        super(Agent, self).__init__(*args, **kwargs)

    business_id = models.CharField(max_length=200)


class User(UserBase):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'USER'
        super(User, self).__init__(*args, **kwargs)

    tags = models.ManyToManyField(Tag)
