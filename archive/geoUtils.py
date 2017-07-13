import geocoder

from . models import Location


def geocode_location_forward(specific_location_string):

    return geocoder.google(specific_location_string)


def geocode_location_backwards(lat, lon):

    return geocoder.google([lat, lon], method = "reverse")

def create_db_location_from_string(location_string):

    location_data = geocode_location_forward(location_string)

    new_location = Location.objects.create(
        full_name = location_string
    )

    if location.city:
        new_location.city = location.city
    if location.state:
        new_location.state = location.state
    if location.county:
        new_location.county = location.county
    if location.country_long:
        new_location.country = location.country_long
    if location.country:
        new_location.iso_alpha_2 = location.country
    if location.lat:
        new_location.lat = location.lat
    if location.lon:
        new_location.lon = location.lon
    
    new_location.save()