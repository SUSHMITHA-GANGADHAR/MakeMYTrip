import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trips.models import Trip, Hotel, Vehicle

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
            "vehicles": [("Luxury Bus", 40), ("Private Cab", 4)],
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
            "vehicles": [("Private Boat", 10), ("E-Rickshaw", 2)],
            "nearby": "Kashi Vishwanath Temple, Dashashwamedh Ghat, Sarnath, Manikarnika Ghat, Assi Ghat, Banaras Hindu University, Ramnagar Fort, Tulsi Manas Mandir, Sankat Mochan Mandir, Dhamek Stupa, Durga Temple"
        },
        {
            "destination": "Khajuraho - Central Indian Heritage",
            "duration": "4 Days / 3 Nights",
            "description": "Explore the UNESCO World Heritage site known for its stunning nagara-style architecture and intricate erotic sculptures.",
            "price": 18500,
            "total_seats": 25,
            "available_seats": 25,
            "image_urls": ["https://images.unsplash.com/photo-1603204000451-f761fc703088?w=800"],
            "hotels": ["The Lalit Temple View"],
            "vehicles": [("Private Sedan", 4)],
            "nearby": "Kandariya Mahadeva Temple, Lakshmana Temple, Vishvanatha Temple, Matangeshwar Temple, Parsvanath Temple, Chaturbhuj Temple, Dulhadeo Temple, Archaeological Museum, Raneh Falls, Panna National Park"
        },
        {
            "destination": "Golden Temple - Amritsar Divine",
            "duration": "3 Days / 2 Nights",
            "description": "Visit the holiest shrine of Sikhism and witness the Indo-Pak border ceremony at Wagah. Includes authentic Punjabi meals.",
            "price": 12000,
            "total_seats": 100,
            "available_seats": 60,
            "image_urls": ["https://images.unsplash.com/photo-1514222139-b576bb5ce007?w=800"],
            "hotels": ["Hyatt Regency Amritsar"],
            "vehicles": [("Luxury Coach", 50)],
            "nearby": "Golden Temple, Jallianwala Bagh, Wagah Border, Partition Museum, Durgiana Temple, Akal Takht, Tarn Taran Sahib, Gobindgarh Fort, Ram Tirath Temple, Maharaja Ranjit Singh Museum"
        },
        {
            "destination": "Tirupati - Balaji Darshan",
            "duration": "2 Days / 1 Night",
            "description": "Seamless VIP Darshan experience at the richest temple in the world. Includes round-trip transport and premium accommodation.",
            "price": 9500,
            "total_seats": 40,
            "available_seats": 40,
            "image_urls": ["https://images.unsplash.com/photo-1620612450335-9003310029b3?w=800"],
            "hotels": ["Fortune Select Grand Ridge"],
            "vehicles": [("Private SUV", 7)],
            "nearby": "Venkateswara Temple, Silathoranam, Akashaganga, Swami Pushkarini, ISKCON Temple, Govindaraja Swami Temple, Kapila Theertham, Sri Padmavathi Ammavari Temple, Regional Science Centre, Deer Park"
        },
        {
            "destination": "Hampi - Ruins of Vijayanagara",
            "duration": "4 Days / 3 Nights",
            "description": "A journey back in time to the capital of the Vijayanagara Empire. Breathtaking stone architecture and river views.",
            "price": 16000,
            "total_seats": 20,
            "available_seats": 15,
            "image_urls": ["https://images.unsplash.com/photo-1506461883276-594a12b11cf3?w=800"],
            "hotels": ["Evolve Back Kamlapura Palace"],
            "vehicles": [("Auto Rickshaw Tour", 3), ("Private Van", 12)],
            "nearby": "Virupaksha Temple, Vittala Temple, Lotus Mahal, Elephant Stables, Hazara Rama Temple, Queen's Bath, Matanga Hill, Tungabhadra River, Sanapur Lake, Anjanadri Hill, Hemakuta Hill, Lakshmi Narasimha Temple"
        },
        {
            "destination": "Konark - The Sun Temple",
            "duration": "3 Days / 2 Nights",
            "description": "Behold the 13th-century Sun Temple designed as a colossal chariot. Visit the scenic Puri beach nearby.",
            "price": 14000,
            "total_seats": 30,
            "available_seats": 30,
            "image_urls": ["https://images.unsplash.com/photo-1590050752117-23a9d7f6e39e?w=800"],
            "hotels": ["Mayfair Heritage Puri"],
            "vehicles": [("Private Taxi", 4)],
            "nearby": "Konark Sun Temple, Chandrabhaga Beach, Puri Jagannath Temple, Chilika Lake, Raghurajpur Craft Village, Daya River, Sakshigopal Temple, Pipli Garden, Konark Museum, Golden Beach"
        },
        {
            "destination": "Rishikesh - Yoga & Divine Ganges",
            "duration": "5 Days / 4 Nights",
            "description": "Experience the spiritual energy of the Himalayas. Visit the Beatles Ashram, participate in Ganga Aarti, and try river rafting.",
            "price": 17500,
            "total_seats": 30,
            "available_seats": 20,
            "image_urls": ["https://images.unsplash.com/photo-1544735745-b89b57c61dfd?w=800"],
            "hotels": ["Taj Rishikesh Resort"],
            "vehicles": [("Mountain SUV", 7)],
            "nearby": "Laxman Jhula, Ram Jhula, Triveni Ghat, Parmarth Niketan, Beatles Ashram, Neer Garh Waterfall, Shivpuri, Vashishta Gufa, Kunjapuri Temple, Rajaji National Park, Har Ki Pauri Haridwar"
        }
    ]

    for data in trips_data:
        Trip.objects.update_or_create(
            destination=data["destination"],
            defaults={
                "duration": data["duration"],
                "description": data["description"],
                "price": data["price"],
                "total_seats": data["total_seats"],
                "available_seats": data["available_seats"],
                "image_url": data["image_urls"][0] if data["image_urls"] else None,
                "nearby_places": data["nearby"]
            }
        )
        if created:
            for hotel_name in data["hotels"]:
                Hotel.objects.create(name=hotel_name, location=trip.destination.split(' - ')[0], trip=trip)
            for v_type, cap in data["vehicles"]:
                Vehicle.objects.create(type=v_type, capacity=cap, trip=trip)
            print(f"Created trip: {trip.destination}")
        else:
            print(f"Trip already exists: {trip.destination}")

if __name__ == "__main__":
    populate()
