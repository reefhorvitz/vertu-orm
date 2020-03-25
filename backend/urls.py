from django.urls import path
from . import views

urlpatterns = [
    path('opentok/<int:appointment_id>/', views.opentok),
    path('login/', views.validate_login),
    path('upload-image/', views.upload_image),
    path('properties/metadata/', views.property_metadata),
    path('properties/', views.create_property),
]
