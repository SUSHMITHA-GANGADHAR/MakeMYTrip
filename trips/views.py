from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trip

def index(request):
    top_trips = Trip.objects.all()[:6] # Get first 6 trips
    return render(request, 'main/index.html', {'top_trips': top_trips})

def splash(request):
    return render(request, 'main/splash.html')

@login_required
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})

from django.conf import settings

@login_required
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    nearby_list = [p.strip() for p in trip.nearby_places.split(',')] if trip.nearby_places else []
    
    context = {
        'trip': trip, 
        'nearby_list': nearby_list,
        'RAZORPAY_KEY_ID': getattr(settings, 'RAZORPAY_KEY_ID', 'rzp_test_XoKjNnQ8mC4u6q')
    }
    return render(request, 'trips/trip_detail.html', context)
