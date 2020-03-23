import json

from django.http import JsonResponse
from rest_framework import serializers
from backend import service
from backend.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


def create_property(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        address_one = body['addressOne']
        address_two = body['addressTwo']
        zip_code = body['zipCode']
        city_id = body['city']
        size = body['size']
        price = body['price']
        seller_id = body['seller']
        year_built = body['yearBuilt']
        bedroom_number = body['bedroomNum']
        bathroom_number = body['bathroomNum']
        heating_id = body['heatingId']
        cooling_id = body['coolingId']
        parking_id = body['parkingId']
        type_id = body['typeId']
        tags_id = body['tagsIds']
        amenities_ids = body['amenitiesIds']
        facilities_ids = body['facilitiesIds']
        other_data_ids = body['otherDataIds']
        images_ids = body['images']
        apartment = service.create_property(address_one, address_two, zip_code, city_id, size, price, seller_id,
                                            year_built, bedroom_number, bathroom_number, heating_id, cooling_id,
                                            parking_id, type_id, tags_id, amenities_ids, facilities_ids,
                                            other_data_ids, images_ids)
        return JsonResponse(PropertySerializer(apartment).data)
