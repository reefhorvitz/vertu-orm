from django.contrib import admin
from .models import User, Appointment, Property, OtherData, Cooling, Tag, Type, Parking, Amenity, Heating, Facility, \
    Location, City, Country, Agent, Image

# Register your models here.

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Amenity)
admin.site.register(Appointment)
admin.site.register(Property)
admin.site.register(OtherData)
admin.site.register(Country)
admin.site.register(Cooling)
admin.site.register(Heating)
admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(Parking)
admin.site.register(Facility)
admin.site.register(Location)
admin.site.register(City)
admin.site.register(Image)
# admin.site.register(AuthUser)
