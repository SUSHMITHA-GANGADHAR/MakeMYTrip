from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    duration = models.CharField(max_length=50) # e.g. "5 Days / 4 Nights"
    start_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    image = models.ImageField(upload_to='trip_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    nearby_places = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.destination

class Hotel(models.Model):
    HOTEL_TYPES = (
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    )
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    hotel_type = models.CharField(max_length=20, choices=HOTEL_TYPES, default='standard')
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='hotels')

    def __str__(self):
        return f"{self.name} ({self.get_hotel_type_display()})"

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('2-wheeler', '2-wheeler'),
        ('3/4-seater', '3/4-seater'),
        ('6-seater', '6-seater'),
        ('TT van / Bus', 'TT van / Bus'),
    )
    type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    capacity = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return self.type
