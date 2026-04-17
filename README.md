# MakeMyTrip Premium - Travel Experience Platform

A state-of-the-art travel booking platform built with Django, featuring a premium "Frosted White Glass" aesthetic and seamless end-to-end mission workflows.

## ✨ Key Features
- **Cinematic UI/UX**: High-end glassmorphism design with backdrop-blur effects and fluid animations.
- **Interactive Booking Engine**: Real-time price calculation based on travel distance, vehicle type (Sedan, SUV, Bus, Flight), and service tiers.
- **Integrated Payments**: Razorpay gateway integration with a failsafe demo-mode for project presentations.
- **Dynamic Inventory**: Automatic seat deduction on booking and restoration on cancellation.
- **Admin Command Center**: Unified dashboard to manage trips, hotels, partners, and approve/reject bookings.
- **Personalized Portal**: Customer dashboard featuring active tickets, travel history, and real-time tracking.

## 🛠 Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Vanilla JS, Glass-CSS, Google Fonts
- **Database**: SQLite (Local) / PostgreSQL (Production)
- **Payments**: Razorpay API
- **Deployment**: Render-ready with WhiteNoise and Gunicorn

## 🔄 Core Workflow

### 1. Discovery & Selection
Users land on a cinematic splash page and browse a curated list of global destinations. Each trip includes high-res imagery and unmissable nearby attractions.

### 2. Interactive Reservation
- **Step 1**: Choose your ride (Flight, Cab, SUV, Bus).
- **Step 2**: Select Service Tier (Standard or ★ Premium ★).
- **Step 3**: Specify Traveler count.
- **Step 4**: Upload Verification documents (Aadhar/Passport).
- **Real-time Math**: The system calculates GST, Service Fees, and Tolls instantly.

### 3. Payment & Confirmation
- Secure payment via Razorpay.
- Upon success, the system captures exact metadata and deducts seats from the global inventory.
- Admin receives a notification to "Approve" the mission.

### 4. Journey Management
- **Customer**: Views active tickets on the dashboard. Can "Terminate Reservation" (Cancel) with an automatic 98% refund calculation.
- **Admin**: Approves bookings, manages hotel properties, and monitors occupancy velocity via analytics charts.

## 🚀 Local Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up `.env` with your `RAZORPAY_KEY` and `RAZORPAY_SECRET`.
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## 🌍 Deployment
This project is pre-configured for **Render**. Simply connect your GitHub repository and the provided `build.sh` will handle the rest.

---
*Created by SUSHMITHA GANGADHAR*
