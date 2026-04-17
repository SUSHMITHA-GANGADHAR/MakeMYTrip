from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from bookings.models import Booking
from trips.models import Trip
from django.conf import settings
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            # Verify the signature
            client.utility.verify_payment_signature(params_dict)
            
            payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
            payment.razorpay_payment_id = razorpay_payment_id
            payment.status = 'success'
            payment.save()

            booking = payment.booking
            booking.is_paid = True
            booking.status = 'payment_confirmed'  # Show payment confirm first
            booking.save()

            # The status will then transition to 'pending_admin' via a signal or we just set it here
            booking.status = 'pending_admin'
            booking.save()

            return render(request, 'payments/success.html', {'booking': booking})
        except Exception as e:
            return render(request, 'payments/failure.html')
    
    return redirect('trips:index')

def mock_payment_success(request, booking_id):
    # Mock success for testing without keys
    booking = Booking.objects.get(id=booking_id)
    booking.is_paid = True
    booking.status = 'payment_confirmed'
    booking.save()
    
    booking.status = 'pending_admin'
    booking.save()
    
    payment, created = Payment.objects.get_or_create(booking=booking)
    payment.status = 'success'
    payment.save()
    
    return render(request, 'payments/success.html', {'booking': booking})
