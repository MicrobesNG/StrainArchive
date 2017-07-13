import geocoder

from . models import Location


def geocode_location_forward(specific_location_string):

    return geocoder.google(specific_location_string)


def geocode_location_backwards(lat, lon):

    return geocoder.google([lat, lon], method = "reverse")

def create_db_location_from_string(location_string):

    location_data = geocode_location_forward(location_string)

    new_location = Location.objects.create(
        
    )