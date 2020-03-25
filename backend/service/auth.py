from backend.models import User, Agent


def validate_login(email, token):
    return User.objects.get(email=email)


def create_user(name, email, password, phone, image):
    return User.objects.create(name=name, email=email, password=password, phone=phone, image=image)


def create_agent(name, email, password, phone, image, business_id):
    return Agent.objects.create(name=name, email=email, password=password, phone=phone, image=image,
                                business_id=business_id)