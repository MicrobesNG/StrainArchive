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

    if location_data.city:
        new_location.city = location_data.city
    if location_data.state:
        new_location.state = location_data.state
    if location_data.county:
        new_location.county = location_data.county
    if location_data.country_long:
        new_location.country = location_data.country_long
    if location_data.country:
        new_location.iso_alpha_2 = location_data.country
    if location_data.lat:
        new_location.lat = location_data.lat
    if location_data.lng:
        new_location.lon = location_data.lng
    
    new_location.save()

def create_db_location_from_coords(lat, lon):

    location_data = geocode_location_backwards(lat, lon)

    new_location = Location.objects.create(
        full_name = location_data.address
    )

    if location_data.city:
        new_location.city = location_data.city
    if location_data.state:
        new_location.state = location_data.state
    if location_data.county:
        new_location.county = location_data.county
    if location_data.country_long:
        new_location.country = location_data.country_long
    if location_data.country:
        new_location.iso_alpha_2 = location_data.country
    if location_data.lat:
        new_location.lat = location_data.lat
    if location_data.lng:
        new_location.lon = location_data.lng

    new_location.save()