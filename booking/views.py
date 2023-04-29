from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .models import Table
from .models import Timeslot
from django.contrib.auth.models import User
from .forms import BookingForm

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
    is_new = True
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data['date']
            table = form.cleaned_data['table']
            timeslot = form.cleaned_data['timeslot']
            is_new = validate_booking(date, table, timeslot)
            if is_new:
                Booking.objects.create(
                    user=user, date=date,
                    table=table,
                    timeslot=timeslot
                    )
                return redirect('Home')
            else:
                form = BookingForm()
                context = {
                    'form': form,
                    'is_new': is_new
                }
                return render(request, 'booking/booking.html', context)
    form = BookingForm()
    context = {
        'form': form,
        'is_new': is_new
    }
    return render(request, 'booking/booking.html', context)


def validate_booking(date, table, timeslot):
    check_booking = Booking.objects.filter(
        date=date, table=table,
        timeslot=timeslot
        )
    if check_booking.__len__() > 0:
        return False
    else:
        return True


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    is_new = True
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data['date']
            table = form.cleaned_data['table']
            timeslot = form.cleaned_data['timeslot']
            is_new = validate_booking(date, table, timeslot)
            if is_new:
                Booking.objects.create(
                    user=user, date=date,
                    table=table,
                    timeslot=timeslot
                    )
                return redirect('Home')
            else:
                form = BookingForm(instance=booking)
                context = {
                    'form': form,
                    'is_new': is_new
                }
                return render(request, 'booking/edit_booking.html', context)
    form = BookingForm(instance=booking)
    context = {
        'form': form,
        'is_new': is_new
    }
    return render(request, 'booking/edit_booking.html', context)
