from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from trips.models import Trip, Hotel
from bookings.models import Booking
from accounts.models import Partner
from django.db.models import Sum

User = get_user_model()

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('dashboard:customer_dashboard')
    
    # Unified Operational Handlers (SPA Action based)
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_trip' or action == 'edit_trip':
            destination = request.POST.get('destination')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image_url = request.POST.get('image_url')
            total_seats = request.POST.get('total_seats', 40)
            
            if action == 'edit_trip':
                trip_id = request.POST.get('trip_id')
                trip = Trip.objects.get(id=trip_id)
                trip.destination = destination
                trip.price = price
                trip.description = description
                trip.image_url = image_url
                trip.total_seats = total_seats
                trip.start_date = request.POST.get('start_date')
                trip.save()
            else:
                Trip.objects.create(
                    destination=destination,
                    price=price,
                    description=description,
                    image_url=image_url,
                    start_date=request.POST.get('start_date'),
                    total_seats=total_seats,
                    available_seats=total_seats,
                    duration="5 Days / 4 Nights"
                )

        elif action == 'add_hotel':
            trip_id = request.POST.get('trip_id')
            trip = Trip.objects.get(id=trip_id)
            Hotel.objects.create(
                trip=trip,
                name=request.POST.get('name'),
                location=request.POST.get('location'),
                hotel_type=request.POST.get('hotel_type'),
                description=request.POST.get('description'),
                price_per_night=request.POST.get('price_per_night', 0)
            )

        elif action == 'confirm_booking':
            booking_id = request.POST.get('booking_id')
            booking = Booking.objects.get(id=booking_id)
            booking.status = 'confirmed'
            booking.save()

        elif action == 'reject_booking':
            booking_id = request.POST.get('booking_id')
            booking = Booking.objects.get(id=booking_id)
            booking.status = 'rejected'
            # Full refund for admin rejection as requested
            booking.refund_amount = booking.total_price
            booking.save()

        elif action == 'add_partner':
            Partner.objects.create(
                name=request.POST.get('name'),
                category=request.POST.get('category'),
                location=request.POST.get('location'),
                image_url=request.POST.get('image_url')
            )

        elif action == 'remove_partner':
            partner_id = request.POST.get('partner_id')
            Partner.objects.filter(id=partner_id).delete()

        return redirect('dashboard:admin_dashboard')

    # Fetch all data for SPA sections
    trips = Trip.objects.all().order_by('-id')
    bookings = Booking.objects.all().order_by('-created_at')
    customers = User.objects.filter(role='customer').order_by('-id')
    all_hotels = Hotel.objects.all().order_by('-id')
    hotel_partners = Partner.objects.filter(category='hotel').order_by('-id')
    travel_partners = Partner.objects.filter(category='travel').order_by('-id')

    total_trips = trips.count()
    total_bookings = bookings.count()
    total_booked_seats = Booking.objects.filter(status='confirmed').aggregate(Sum('seats_booked'))['seats_booked__sum'] or 0
    total_capacity = Trip.objects.aggregate(Sum('total_seats'))['total_seats__sum'] or 0
    vacant_seats = total_capacity - total_booked_seats

    context = {
        'total_trips': total_trips,
        'total_bookings': total_bookings,
        'booked_seats': total_booked_seats,
        'vacant_seats': vacant_seats,
        'all_trips': trips,
        'all_bookings': bookings,
        'all_customers': customers,
        'all_hotels': all_hotels,
        'hotel_partners': hotel_partners,
        'travel_partners': travel_partners,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def customer_dashboard(request):
    if request.user.role == 'admin':
        return redirect('dashboard:admin_dashboard')
    
    from django.utils import timezone
    now = timezone.now().date()
    
    available_trips = Trip.objects.all()
    all_user_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    
    # Active: Pending/Confirmed and trip has not yet started/ended
    active_bookings = all_user_bookings.filter(
        status__in=['payment_confirmed', 'pending_admin', 'confirmed']
    ).exclude(trip__start_date__lt=now)
    
    # History: Rejected, Cancelled, or Confirm trips that have already happened (start_date < now)
    history_bookings = all_user_bookings.filter(
        models.Q(status__in=['cancelled', 'rejected']) | 
        models.Q(status='confirmed', trip__start_date__lt=now)
    )
    
    context = {
        'available_trips': available_trips,
        'active_bookings': active_bookings,
        'history_bookings': history_bookings,
        'has_bookings': all_user_bookings.exists(),
    }
    return render(request, 'dashboard/customer_dashboard.html', context)
