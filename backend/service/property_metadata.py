from backend.models import Amenity, Facility, OtherData, Type, Heating, Cooling, Parking, Tag, City, Country


def get_all_property_metadata():
    result = {}
    result['amenities'] = list(Amenity.objects.all().values('id', 'name'))
    result['facilities'] = list(Facility.objects.all().values('id', 'name'))
    result['tags'] = list(Tag.objects.all().values('id', 'name'))
    result['otherData'] = list(OtherData.objects.all().values('id', 'name'))
    result['types'] = list(Type.objects.all().values('id', 'name'))
    result['heating'] = list(Heating.objects.all().values('id', 'name'))
    result['cooling'] = list(Cooling.objects.all().values('id', 'name'))
    result['parking'] = list(Parking.objects.all().values('id', 'name'))
    result['cities'] = list(City.objects.all().values('id', 'name'))
    result['countries'] = list(Country.objects.all().values('id', 'name'))
    return result
