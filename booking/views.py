from django.shortcuts import render
from .models import Booking

# Create your views here.


def home_page(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/index.html', context)


def open_contacts(request):
    return render(request, 'booking/contacts.html')


def make_booking(request):
    return render(request, 'booking/booking.html')
