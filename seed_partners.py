import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import Partner

def seed_partners():
    partners = [
        {'name': 'Marriott International', 'category': 'hotel', 'location': 'Maryland, USA'},
        {'name': 'Hilton Worldwide', 'category': 'hotel', 'location': 'Virginia, USA'},
        {'name': 'Expedia Group', 'category': 'travel', 'location': 'Washington, USA'},
        {'name': 'Emirates', 'category': 'travel', 'location': 'Dubai, UAE'},
    ]

    for p in partners:
        Partner.objects.get_or_create(
            name=p['name'],
            category=p['category'],
            defaults={'location': p['location']}
        )
    print("Seeded 4 worldwide partners successfully.")

if __name__ == '__main__':
    seed_partners()
