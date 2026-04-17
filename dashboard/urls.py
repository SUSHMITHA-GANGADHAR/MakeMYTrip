from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.admin_dashboard, name='index'), # Mapping index to admin_dashboard for now
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
]
