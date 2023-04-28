from django.shortcuts import render
from .models import Booking
from .models import Table
from .models import Timeslot

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
    tables = Table.objects.all()
    timeslots = Timeslot.objects.all()
    context = {
        'tables': tables,
        'timeslots': timeslots
    }
    return render(request, 'booking/booking.html', context)
