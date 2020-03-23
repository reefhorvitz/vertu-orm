from backend.models import Location, Agent, Heating, Cooling, Parking, Type, Tag, Amenity, Facility, OtherData, \
    Property, Image


def create_property(address_one, address_two, zip_code, city_id, size, price, seller_id, year_built, bedroom_number, bathroom_number, heating_id,
                    cooling_id, parking_id, type_id, tags_id, amenities_ids, facilities_ids, other_data_ids,
                    images_ids):
    location = Location.objects.create(city_id=city_id, address_one=address_one, address_two=address_two,
                                       zip_code=zip_code)
    tags = map(lambda tag_id: Tag.objects.get(pk=tag_id), tags_id)
    amenities = map(lambda amenity_id: Amenity.objects.get(pk=amenity_id), amenities_ids)
    facilities = map(lambda facility_id: Facility.objects.get(pk=facility_id), facilities_ids)
    other_data = map(lambda other_data_id: OtherData.objects.get(pk=other_data_id), other_data_ids)
    images = map(lambda image_id: Image.objects.get(pk=image_id), images_ids)

    apartment = Property.objects.create(location_id=location.id, size=size, price=price, seller_id=seller_id,
                                        year_built=year_built, bedroom_number=bedroom_number,
                                        bathroom_number=bathroom_number, heating_id=heating_id, cooling_id=cooling_id,
                                        parking_id=parking_id, type_id=type_id)

    apartment.tags.add(*tags)
    apartment.amenities.add(*amenities)
    apartment.facilities.add(*facilities)
    apartment.other_data.add(*other_data)
    apartment.images.add(*images)
    return apartment
