import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trips.models import Trip, Hotel

def populate_hotels():
    trips = Trip.objects.all()
    for trip in trips:
        # Create a Standard Hotel
        Hotel.objects.get_or_create(
            trip=trip,
            hotel_type='standard',
            name=f"{trip.destination} Comfort Inn",
            location=f"Central {trip.destination}",
            price_per_night=1500,
            description="Clean rooms, free breakfast, and central location."
        )
        
        # Create a Premium Hotel
        Hotel.objects.get_or_create(
            trip=trip,
            hotel_type='premium',
            name=f"The {trip.destination} Grand Plaza",
            location=f"Luxury Row, {trip.destination}",
            price_per_night=4500,
            description="5-star luxury, infinity pool, gourmet dining, and private butler service."
        )
    print("Sucessfully populated standard and premium hotels for all trips.")

if __name__ == '__main__':
    populate_hotels()
