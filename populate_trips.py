import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trips.models import Trip, Hotel
from accounts.models import Partner

def populate():
    trips_data = [
        {
            "destination": "Paris Romance (International Flight)",
            "duration": "7 Days / 6 Nights",
            "description": "The ultimate European getaway. Includes Eiffel Tower tours, Louvre visits, and luxury stays in central Paris. Experience the romance of the Seine and the world's finest art collections.",
            "price": 45000,
            "total_seats": 20,
            "available_seats": 12,
            "image_url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1000",
            "hotels": ["The Ritz Paris", "Hotel Plaza Athenee"],
            "nearby": "Eiffel Tower, Louvre Museum, Notre-Dame, Montmartre"
        },
        {
            "destination": "Goa - The Party Capital",
            "duration": "4 Days / 3 Nights",
            "description": "Sun, sand, and serenity. Experience the best of North Goa's nightlife and South Goa's quiet white-sand beaches. Enjoy authentic Konkani cuisine and heritage vibes.",
            "price": 9500,
            "total_seats": 100,
            "available_seats": 85,
            "image_url": "https://images.unsplash.com/photo-1512783563744-1921f6690460?w=1000",
            "hotels": ["Taj Exotica Goa", "W Goa"],
            "nearby": "Baga Beach, Calangute Beach, Fort Aguada, Old Goa"
        },
        {
            "destination": "Leh Ladakh - Adventure Paradise",
            "duration": "7 Days / 6 Nights",
            "description": "A journey through the land of high passes. Visit the impossibly blue Pangong Lake, the cold desert of Nubra Valley, and the highest motorable road at Khardung La.",
            "price": 32000,
            "total_seats": 40,
            "available_seats": 25,
            "image_url": "https://images.unsplash.com/photo-1581791534721-e5993446d788?w=1000",
            "hotels": ["The Grand Dragon", "Ladakh Sarai"],
            "nearby": "Pangong Lake, Hemis Monastery, Nubra Valley"
        },
        {
            "destination": "Luxury Sleeper: Bangalore to Mumbai",
            "duration": "1 Night / 1 Day",
            "description": "Travel in the most premium sleeper bus with personal screens, fully flat beds, and in-bus meals. The most comfortable way to cross the Deccan plateau.",
            "price": 3500,
            "total_seats": 30,
            "available_seats": 18,
            "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=1000",
            "hotels": [],
            "nearby": "Western Ghats, Coastal Views, Expressway"
        },
        {
            "destination": "Kerala - God's Own Country",
            "duration": "5 Days / 4 Nights",
            "description": "Paradise of backwaters and lush greenery. Enjoy a stay on a traditional houseboat in Alleppey and visit the mist-covered tea gardens of Munnar.",
            "price": 18500,
            "total_seats": 50,
            "available_seats": 35,
            "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1000",
            "hotels": ["Kumarakom Lake Resort", "The Zuri"],
            "nearby": "Alleppey Backwaters, Munnar Tea Gardens, Thekkady"
        },
        {
            "destination": "Spiritual South: Meenakshi & Madurai",
            "duration": "5 Days / 4 Nights",
            "description": "A deep dive into the Dravidian architecture of Tamil Nadu. Visit the ancient Meenakshi Temple and experience pure luxury stay with rich heritage.",
            "price": 22000,
            "total_seats": 50,
            "available_seats": 35,
            "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=1000",
            "hotels": ["Taj Madurai", "Heritage Madurai"],
            "nearby": "Meenakshi Amman Temple, Thirumalai Nayakkar Mahal"
        },
        {
            "destination": "Hampi - Ruins of Vijayanagara",
            "duration": "4 Days / 3 Nights",
            "description": "A journey back in time to the capital of the Vijayanagara Empire. Breathtaking stone architecture, boulder-strewn landscapes, and ancient whispers.",
            "price": 16000,
            "total_seats": 25,
            "available_seats": 15,
            "image_url": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?w=1000",
            "hotels": ["Evolve Back Kamlapura Palace"],
            "nearby": "Virupaksha Temple, Vittala Temple, Lotus Mahal"
        },
        {
            "destination": "Varanasi - The Eternal City",
            "duration": "3 Days / 2 Nights",
            "description": "Witness the world-famous Ganga Aarti and explore the narrow lanes of the world's oldest living city. Experience a sunrise boat ride on the holy Ganges.",
            "price": 15000,
            "total_seats": 30,
            "available_seats": 20,
            "image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?w=1000",
            "hotels": ["Brijrama Palace", "Taj Ganges"],
            "nearby": "Kashi Vishwanath Temple, Dashashwamedh Ghat"
        },
        {
            "destination": "Golden Temple - Amritsar Divine",
            "duration": "3 Days / 2 Nights",
            "description": "Visit the holiest shrine of Sikhism and witness the Indo-Pak border ceremony at Wagah. Experience the world's largest community kitchen.",
            "price": 12000,
            "total_seats": 100,
            "available_seats": 60,
            "image_url": "https://images.unsplash.com/photo-1514222139-b576bb5ce007?w=1000",
            "hotels": ["Hyatt Regency Amritsar"],
            "nearby": "Golden Temple, Jallianwala Bagh, Wagah Border"
        },
        {
            "destination": "Konark - The Sun Temple",
            "duration": "3 Days / 2 Nights",
            "description": "Behold the 13th-century Sun Temple designed as a colossal chariot. Visit the scenic Puri beach and witness the intricate stone carvings.",
            "price": 14000,
            "total_seats": 30,
            "available_seats": 30,
            "image_url": "https://images.unsplash.com/photo-1590050752117-23a9d7f6e39e?w=1000",
            "hotels": ["Mayfair Heritage Puri"],
            "nearby": "Konark Sun Temple, Chandrabhaga Beach, Puri"
        },
        {
            "destination": "Rishikesh - Yoga & Divine Ganges",
            "duration": "5 Days / 4 Nights",
            "description": "Experience the spiritual energy of the Himalayas. Visit the Beatles Ashram, witness the evening Ganga Aarti, and try exhilarating river rafting.",
            "price": 17500,
            "total_seats": 35,
            "available_seats": 25,
            "image_url": "https://images.unsplash.com/photo-1544735745-b89b57c61dfd?w=1000",
            "hotels": ["Taj Rishikesh Resort"],
            "nearby": "Laxman Jhula, Ram Jhula, Beatles Ashram"
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

    # Seed Partners
    Partner.objects.update_or_create(name="Taj Hotels", defaults={"category": "hotel", "location": "Mumbai, India"})
    Partner.objects.update_or_create(name="IndiGo Airlines", defaults={"category": "travel", "location": "Delhi, India"})
    Partner.objects.update_or_create(name="Uber Luxury", defaults={"category": "travel", "location": "Bangalore, India"})

if __name__ == "__main__":
    populate()
