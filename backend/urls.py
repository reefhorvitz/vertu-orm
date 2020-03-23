from django.urls import path
from . import views

urlpatterns = [
    path('opentok/<int:appointment_id>/', views.opentok),
    path('properties/metadata/', views.property_metadata),
    path('properties/', views.create_property),
]
