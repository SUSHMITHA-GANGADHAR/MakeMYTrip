from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        role = request.POST.get('role', 'customer')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('accounts:register')
        
        user = CustomUser.objects.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
            role=role
        )
        messages.success(request, f'Account for {name} created successfully! Please login to continue.')
        return redirect('accounts:login')
    
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            
            if user.role == 'admin':
                return redirect('dashboard:admin_dashboard')
            else:
                return redirect('dashboard:customer_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('trips:index')

def forgot_password(request):
    # logic for forgot password
    return render(request, 'accounts/forgot_password.html')

def reset_password(request, token):
    # logic for reset password
    return render(request, 'accounts/reset_password.html')
