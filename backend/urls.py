from django.urls import path
from . import views

urlpatterns = [
    path('opentok/<int:appointment_id>/', views.OpenTok.as_view()),
    path('login/', views.validate_login),
    path('appointments/', views.Appointments.as_view()),
    path('upload-image/', views.UploadImage.as_view()),
    path('properties/metadata/', views.PropertyMetadata.as_view()),
    path('properties/', views.Property.as_view()),
    path('users/', views.UserList.as_view()),
]
