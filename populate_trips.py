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
            "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Taj Madurai", "Heritage Madurai"],
            "nearby": "Meenakshi Amman Temple, Thirumalai Nayakkar Mahal"
        },
        {
            "destination": "Varanasi - The Eternal City",
            "duration": "3 Days / 2 Nights",
            "description": "Witness the world-famous Ganga Aarti and explore the narrow lanes of the world's oldest living city. Divine North Indian experience.",
            "price": 15000,
            "total_seats": 30,
            "available_seats": 20,
            "image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Brijrama Palace", "Taj Ganges"],
            "nearby": "Kashi Vishwanath Temple, Dashashwamedh Ghat"
        },
        {
            "destination": "Paris Romance (International Flight)",
            "duration": "7 Days / 6 Nights",
            "description": "The ultimate European getaway. Includes Eiffel Tower tours, Louvre visits, and luxury stays in central Paris.",
            "price": 45000,
            "total_seats": 20,
            "available_seats": 12,
            "image_url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
            "hotels": ["The Ritz Paris", "Hotel Plaza Athenee"],
            "nearby": "Eiffel Tower, Louvre Museum"
        },
        {
            "destination": "Goa - The Party Capital",
            "duration": "4 Days / 3 Nights",
            "description": "Sun, sand, and serenity. Experience the best of North Goa's nightlife and South Goa's quiet beaches.",
            "price": 9500,
            "total_seats": 100,
            "available_seats": 85,
            "image_url": "https://images.unsplash.com/photo-1512783563744-1921f6690460?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Taj Exotica Goa", "W Goa"],
            "nearby": "Baga Beach, Calangute Beach"
        },
        {
            "destination": "Golden Temple - Amritsar Divine",
            "duration": "3 Days / 2 Nights",
            "description": "Visit the holiest shrine of Sikhism and witness the Indo-Pak border ceremony at Wagah.",
            "price": 12000,
            "total_seats": 100,
            "available_seats": 60,
            "image_url": "https://images.unsplash.com/photo-1514222139-b576bb5ce007?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Hyatt Regency Amritsar"],
            "nearby": "Golden Temple, Jallianwala Bagh"
        },
        {
            "destination": "Hampi - Ruins of Vijayanagara",
            "duration": "4 Days / 3 Nights",
            "description": "A journey back in time to the capital of the Vijayanagara Empire. Breathtaking stone architecture.",
            "price": 16000,
            "total_seats": 25,
            "available_seats": 15,
            "image_url": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Evolve Back Kamlapura Palace"],
            "nearby": "Virupaksha Temple, Vittala Temple"
        },
        {
            "destination": "Konark - The Sun Temple",
            "duration": "3 Days / 2 Nights",
            "description": "Behold the 13th-century Sun Temple designed as a colossal chariot. Visit the scenic Puri beach.",
            "price": 14000,
            "total_seats": 30,
            "available_seats": 30,
            "image_url": "https://images.unsplash.com/photo-1505342412152-3201405b0854?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Mayfair Heritage Puri"],
            "nearby": "Konark Sun Temple, Chandrabhaga Beach"
        },
        {
            "destination": "Rishikesh - Yoga & Divine Ganges",
            "duration": "5 Days / 4 Nights",
            "description": "Experience the spiritual energy of the Himalayas. Visit the Beatles Ashram and try river rafting.",
            "price": 17500,
            "total_seats": 35,
            "available_seats": 25,
            "image_url": "https://images.unsplash.com/photo-1544735745-b89b57c61dfd?auto=format&fit=crop&w=800&q=80",
            "hotels": ["Taj Rishikesh Resort"],
            "nearby": "Laxman Jhula, Ram Jhula"
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
                "image_url": data["image_url"],
                "nearby_places": data["nearby"]
            }
        )
        for hotel_name in data.get("hotels", []):
            Hotel.objects.get_or_create(name=hotel_name, trip=trip, defaults={'location': trip.destination.split(':')[0]})
        print(f"Set up trip: {trip.destination}")

if __name__ == "__main__":
    populate()
