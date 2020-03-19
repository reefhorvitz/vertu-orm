from django.db import models

from backend.models.common import Location
from backend.models.property_metadata import Heating, Cooling, Tag, Amenity, Facility, Parking, OtherData, Type
from backend.models.user import User


class Property(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    size = models.IntegerField('Size in sqft')
    price = models.IntegerField('price $/Month')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    year_built = models.IntegerField('Year built')
    bedroom_number = models.IntegerField()
    bathroom_number = models.FloatField()
    heating = models.ForeignKey(Heating, on_delete=models.CASCADE)
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='properties')
    amenities = models.ManyToManyField(Amenity, related_name='properties')
    facilities = models.ManyToManyField(Facility, related_name='properties')
    other_data = models.ManyToManyField(OtherData, related_name='properties')

    def __str__(self):
        return f'{self.type.name} at {self.location.city} by {self.seller}'

