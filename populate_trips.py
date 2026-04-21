import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trips.models import Trip, Hotel
from accounts.models import Partner

def populate():
    # CLEAR OLD DATA TO REMOVE DUPLICATES
    print("Clearing old inventory for a fresh start...")
    Hotel.objects.all().delete()
    Trip.objects.all().delete()

    trips_data = [
        {
            "destination": "Paris Romance (International Flight)",
            "duration": "7 Days / 6 Nights",
            "description": "The ultimate European getaway. Includes Eiffel Tower tours and Louvre visits.",
            "price": 45000,
            "total_seats": 20,
            "available_seats": 20,
            "image_url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200",
            "hotels": ["The Ritz Paris"],
            "nearby": "Eiffel Tower, Louvre"
        },
        {
            "destination": "Goa - The Party Capital",
            "duration": "4 Days / 3 Nights",
            "description": "Sun, sand, and serenity. Experience the best of North Goa's nightlife.",
            "price": 8500,
            "total_seats": 100,
            "available_seats": 100,
            "image_url": "https://images.unsplash.com/photo-1512783563744-1921f6690460?w=1200",
            "hotels": ["Taj Exotica"],
            "nearby": "Baga Beach"
        },
        {
            "destination": "Leh Ladakh - Adventure Paradise",
            "duration": "7 Days / 6 Nights",
            "description": "Journey through the land of high passes. Visit Pangong Lake and Nubra Valley.",
            "price": 32000,
            "total_seats": 40,
            "available_seats": 40,
            "image_url": "https://images.unsplash.com/photo-1581791534721-e5993446d788?w=1200",
            "hotels": ["The Grand Dragon"],
            "nearby": "Pangong Lake"
        },
        {
            "destination": "Kerala - God's Own Country",
            "duration": "5 Days / 4 Nights",
            "description": "Paradise of backwaters and lush greenery. Stay on a houseboat in Alleppey.",
            "price": 18500,
            "total_seats": 50,
            "available_seats": 50,
            "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1200",
            "hotels": ["Zuri Kumarakom"],
            "nearby": "Alleppey"
        },
        {
            "destination": "Luxury Sleeper: Bangalore to Mumbai",
            "duration": "1 Night / 1 Day",
            "description": "Travel in the most premium sleeper bus with personal screens and fully flat beds.",
            "price": 3500,
            "total_seats": 30,
            "available_seats": 30,
            "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=1200",
            "hotels": [],
            "nearby": "Western Ghats"
        },
        {
            "destination": "Spiritual South: Meenakshi & Madurai",
            "duration": "5 Days / 4 Nights",
            "description": "A deep dive into the Dravidian architecture of Tamil Nadu. Visit the ancient Meenakshi Temple.",
            "price": 22000,
            "total_seats": 50,
            "available_seats": 50,
            "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=1200",
            "hotels": ["Heritage Madurai"],
            "nearby": "Meenakshi Amman Temple"
        },
        {
            "destination": "Puri Jagannath Temple",
            "duration": "3 Days / 2 Nights",
            "description": "Visit the world-famous Jagannath Temple, one of the Char Dham pilgrimage sites.",
            "price": 19500,
            "total_seats": 40,
            "available_seats": 40,
            "image_url": "https://images.unsplash.com/photo-1594991471329-87a710207399?w=1200",
            "hotels": ["Sterling Puri"],
            "nearby": "Jagannath Temple"
        },
        {
            "destination": "Varanasi - The Eternal City",
            "duration": "3 Days / 2 Nights",
            "description": "Witness the world-famous Ganga Aarti and explore the narrow lanes of the oldest city.",
            "price": 15000,
            "total_seats": 30,
            "available_seats": 30,
            "image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?w=1200",
            "hotels": ["Brijrama Palace"],
            "nearby": "Ganga Aarti"
        },
        {
            "destination": "Golden Temple - Amritsar Divine",
            "duration": "3 Days / 2 Nights",
            "description": "Visit the holiest shrine of Sikhism and witness the Wagah border ceremony.",
            "price": 12000,
            "total_seats": 100,
            "available_seats": 100,
            "image_url": "https://images.unsplash.com/photo-1514222139-b576bb5ce007?w=1200",
            "hotels": ["Hyatt Amritsar"],
            "nearby": "Golden Temple"
        },
        {
            "destination": "Hampi - Ruins of Vijayanagara",
            "duration": "4 Days / 3 Nights",
            "description": "A journey back in time to the capital of the Vijayanagara Empire.",
            "price": 16000,
            "total_seats": 25,
            "available_seats": 25,
            "image_url": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?w=1200",
            "hotels": ["Evolve Back Hampi"],
            "nearby": "Stone Chariot"
        },
        {
            "destination": "Konark - The Sun Temple",
            "duration": "3 Days / 2 Nights",
            "description": "Behold the 13th-century Sun Temple designed as a colossal chariot.",
            "price": 14000,
            "total_seats": 30,
            "available_seats": 30,
            "image_url": "https://images.unsplash.com/photo-1590050752117-23a9d7f6e39e?w=1200",
            "hotels": ["Mayfair Heritage"],
            "nearby": "Sun Temple"
        },
        {
            "destination": "Rishikesh - Yoga & Divine Ganges",
            "duration": "5 Days / 4 Nights",
            "description": "Experience the spiritual energy of the Himalayas and the divine Ganges.",
            "price": 17500,
            "total_seats": 35,
            "available_seats": 35,
            "image_url": "https://images.unsplash.com/photo-1544735745-b89b57c61dfd?w=1200",
            "hotels": ["Taj Rishikesh"],
            "nearby": "Beatles Ashram"
        }
    ]

    for data in trips_data:
        trip = Trip.objects.create(
            destination=data["destination"],
            duration=data["duration"],
            description=data["description"],
            price=data["price"],
            total_seats=data["total_seats"],
            available_seats=data["available_seats"],
            image_url=data["image_url"],
            nearby_places=data["nearby"]
        )
        for hotel_name in data.get("hotels", []):
            Hotel.objects.create(name=hotel_name, trip=trip, location=trip.destination.split(' ')[0])
        print(f"Set up trip: {trip.destination}")

    # Seed Partners
    Partner.objects.update_or_create(name="Taj Hotels", defaults={"category": "hotel", "location": "Mumbai, India"})
    Partner.objects.update_or_create(name="IndiGo Airlines", defaults={"category": "travel", "location": "Delhi, India"})

if __name__ == "__main__":
    populate()
