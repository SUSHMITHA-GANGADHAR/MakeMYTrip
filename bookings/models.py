from django.db import models
from django.conf import settings
from trips.models import Trip

class Booking(models.Model):
    STATUS_CHOICES = (
        ('payment_confirmed', 'Paid'),
        ('pending_admin', 'Pending Admin Confirmation'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending_admin')
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for {self.user.email}"
