import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trips.models import Trip, Hotel
from accounts.models import Partner

def populate():
    trips_data = [
        {
            "destination": "Spiritual South: Meenakshi & Madurai",
            "duration": "5 Days / 4 Nights",
            "description": "A deep dive into the Dravidian architecture of Tamil Nadu. Visit the ancient Meenakshi Temple and experience pure luxury stay.",
            "price": 22000,
            "total_seats": 50,
            "available_seats": 35,
            "image_urls": ["https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800"],
            "hotels": ["Taj Madurai", "Heritage Madurai"],
            "nearby": "Meenakshi Amman Temple, Thirumalai Nayakkar Mahal, Alagarkoil Temple, Gandhi Memorial Museum, Vandiyur Mariamman Teppakulam, Samanar Hills, Koodal Azhagar Temple, Pazhamudhir Cholai, Vaigai Dam, St. Mary's Cathedral"
        },
        {
            "destination": "Varanasi - The Eternal City",
            "duration": "3 Days / 2 Nights",
            "description": "Witness the world-famous Ganga Aarti and explore the narrow lanes of the world's oldest living city. Divine North Indian experience.",
            "price": 15000,
            "total_seats": 30,
            "available_seats": 20,
            "image_urls": ["https://images.unsplash.com/photo-1561359313-0639aad49ca6?w=800"],
            "hotels": ["Brijrama Palace", "Taj Ganges"],
            "nearby": "Kashi Vishwanath Temple, Dashashwamedh Ghat, Sarnath, Manikarnika Ghat, Assi Ghat, Banaras Hindu University, Ramnagar Fort, Tulsi Manas Mandir, Sankat Mochan Mandir, Dhamek Stupa, Durga Temple"
        },
        {
            "destination": "Paris Romance (International Flight)",
            "duration": "7 Days / 6 Nights",
            "description": "The ultimate European getaway. Includes Eiffel Tower tours, Louvre visits, and luxury stays in central Paris.",
            "price": 45000,
            "total_seats": 20,
            "available_seats": 12,
            "image_url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800",
            "hotels": ["The Ritz Paris", "Hotel Plaza Athenee"],
            "nearby": "Eiffel Tower, Louvre Museum, Notre-Dame, Arc de Triomphe, Montmartre, Seine River Cruise, Palace of Versailles, Musee d'Orsay, Champs-Elysees, Luxembourg Gardens"
        },
        {
            "destination": "Goa - The Party Capital",
            "duration": "4 Days / 3 Nights",
            "description": "Sun, sand, and serenity. Experience the best of North Goa's nightlife and South Goa's quiet beaches.",
            "price": 9500,
            "total_seats": 100,
            "available_seats": 85,
            "image_url": "https://images.unsplash.com/photo-1512783563744-1921f6690460?w=800",
            "hotels": ["Taj Exotica Goa", "W Goa"],
            "nearby": "Baga Beach, Calangute Beach, Fort Aguada, Dudhsagar Falls, Basilica of Bom Jesus, Anjuna Beach, Old Goa, Vagator Beach, Chapora Fort, Dona Paula"
        }
    ]

    for data in trips_data:
        trip, created = Trip.objects.update_or_create(
            destination=data["destination"],
            defaults={
                "duration": data["duration"],
                "description": data["description"],
                "price": data["price"],
                "total_seats": data["total_seats"],
                "available_seats": data["available_seats"],
                "image_url": data.get("image_url") or (data["image_urls"][0] if data.get("image_urls") else None),
                "nearby_places": data.get("nearby", "")
            }
        )
        
        # Add hotels
        for hotel_name in data.get("hotels", []):
            Hotel.objects.get_or_create(name=hotel_name, trip=trip, defaults={'location': trip.destination.split(':')[0]})
        
        print(f"Set up trip: {trip.destination}")

    # Seed Partners
    Partner.objects.update_or_create(name="Taj Hotels", defaults={"category": "hotel", "location": "Mumbai, India"})
    Partner.objects.update_or_create(name="IndiGo Airlines", defaults={"category": "travel", "location": "Delhi, India"})
    Partner.objects.update_or_create(name="Uber Luxury", defaults={"category": "travel", "location": "Bangalore, India"})

if __name__ == "__main__":
    populate()
