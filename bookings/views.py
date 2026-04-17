from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from trips.models import Trip
from .models import Booking
from payments.models import Payment
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
import razorpay
import json
from django.http import JsonResponse

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        seats = int(request.POST.get('seats', 1))
        total_price = trip.price * seats
        
        if seats > trip.available_seats:
            messages.error(request, 'Not enough seats available!')
            return redirect('dashboard:customer_dashboard')
        
        booking = Booking.objects.create(
            user=request.user,
            trip=trip,
            seats_booked=seats,
            total_price=total_price,
            status='pending_admin'
        )
        
        # Deduct and Save Seats
        trip.available_seats -= seats
        trip.save()
        
        # Razorpay Order Creation
        data = {
            "amount": int(total_price * 100), # amount in paise
            "currency": "INR",
            "receipt": f"receipt_{booking.id}"
        }
        
        try:
            razorpay_order = client.order.create(data=data)
            booking_payment = Payment.objects.create(
                booking=booking,
                amount=total_price,
                razorpay_order_id=razorpay_order['id'],
                status='pending'
            )
            
            context = {
                'booking': booking,
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': total_price,
            }
            return render(request, 'payments/checkout.html', context)
        except Exception as e:
            # Fallback for mock if keys are missing
            return render(request, 'payments/mock_payment.html', {'booking': booking})
            
    return render(request, 'bookings/booking_form.html', {'trip': trip})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status in ['confirmed', 'payment_confirmed', 'pending_admin']:
        # Logic for refund calculation
        now = timezone.now()
        
        # Deduction rules
        from decimal import Decimal
        deduction = Decimal('0.02') # 2% deduction 
        
        booking.refund_amount = booking.total_price * (1 - deduction)
        booking.status = 'cancelled'
        booking.save()
        
        # Restore seats
        booking.trip.available_seats += booking.seats_booked
        booking.trip.save()
        
        messages.success(request, f'Booking cancelled. Refund of ₹{booking.refund_amount} initiated ({deduction*100}% deduction).')
    
    return redirect('dashboard:customer_dashboard')

@csrf_exempt
@login_required
def create_booking_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        trip_id = data.get('trip_id')
        seats = int(data.get('seats', 1))
        total_price = float(data.get('total_price', 0))
        
        trip = get_object_or_404(Trip, id=trip_id)
        
        booking = Booking.objects.create(
            user=request.user,
            trip=trip,
            seats_booked=seats,
            total_price=total_price,
            status='payment_confirmed',
            is_paid=True
        )
        
        # Deduct and Save Seats
        trip.available_seats -= seats
        trip.save()
        
        messages.success(request, 'Payment Successful! Your booking is now pending admin approval.')
        return JsonResponse({'status': 'success', 'booking_id': booking.id})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
@login_required
def initiate_payment_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount_in_paise = 100 
        
        try:
            order_data = {
                "amount": amount_in_paise,
                "currency": "INR",
                "payment_capture": 1
            }
            razorpay_order = client.order.create(data=order_data)
            return JsonResponse({
                'status': 'success',
                'order_id': razorpay_order['id'],
                'amount': amount_in_paise
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error'}, status=400)
