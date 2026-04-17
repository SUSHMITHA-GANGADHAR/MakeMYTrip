from django.urls import path
from . import views

urlpatterns = [
    path('callback/', views.payment_callback, name='payment_callback'),
    path('mock-success/<int:booking_id>/', views.mock_payment_success, name='mock_payment_success'),
]
