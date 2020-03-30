from backend.models import UserBase


def edit_user_details(id, name, phone, email):
    user = UserBase.objects.get(pk=id)
    user.name = name
    user.phone = phone
    user.email = email
    user.save()
    return user
