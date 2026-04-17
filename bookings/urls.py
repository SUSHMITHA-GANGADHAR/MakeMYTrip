from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<int:trip_id>/', views.book_trip, name='book_trip'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('api/create/', views.create_booking_api, name='api_create_booking'),
    path('api/initiate-payment/', views.initiate_payment_api, name='initiate_payment'),
]
