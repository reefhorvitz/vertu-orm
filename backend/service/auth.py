from backend.models import User, Agent, UserBase
from django.shortcuts import get_object_or_404


def validate_login(email, token, password):
    # TODO: add token validation
    user = get_object_or_404(UserBase, email=email)
    return user


def create_user(name, email, password, phone, image):
    return User.objects.create(name=name, email=email, password=password, phone=phone, image=image)


def create_agent(name, email, password, phone, image, business_id):
    return Agent.objects.create(name=name, email=email, password=password, phone=phone, image=image,
                                business_id=business_id)
