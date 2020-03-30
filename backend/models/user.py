# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
from django.db import models
from backend.models.common import Image
from backend.models.property_metadata import Tag
# from orm import settings
# from django.utils.translation import ugettext_lazy as _


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, **extra_fields):
#         return self._create_user(email, password, False, False, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         user = self._create_user(email, password, True, True, **extra_fields)
#         return user
#
#
# class AuthUser(AbstractUser):
#     """User model."""
#
#     username = models.CharField(max_length=200, null=True, blank=True)
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = "Auth User"


class UserBase(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=100)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Agent(UserBase):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'AGENT'
        super(Agent, self).__init__(*args, **kwargs)

    business_id = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Agent"


class User(UserBase):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'USER'
        super(User, self).__init__(*args, **kwargs)

    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Client"
