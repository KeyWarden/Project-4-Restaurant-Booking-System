from django.shortcuts import render, redirect
from .models import Booking
from .models import Table
from .models import Timeslot
from django.contrib.auth.models import User

# Create your views here.


def home_page(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/index.html', context)


def open_contacts(request):
    return render(request, 'booking/contacts.html')

# REMEMBER, FIX DATE VALIDATION
def make_booking(request):
    if request.method == 'POST':
        date = request.POST.get('date_name')
        table_size = request.POST.get('size_name')
        time = request.POST.get('time_name')
        timeslots = Timeslot.objects.filter(time=time)
        timeslots_list = []
        for instance in timeslots:
            timeslots_list.append(instance)
        timeslot = timeslots_list[0]
        table_id = get_table(date, table_size, timeslot)
        user = request.user
        if table_id != 0:
            table = Table.objects.get(pk=table_id)
            Booking.objects.create(
                user=user, date=date, table=table, timeslot=timeslot
                )

            return redirect('Home')
        elif table_id == 0:
            return redirect('Make Booking')
    tables = Table.objects.all()
    timeslots = Timeslot.objects.all()
    context = {
        'tables': tables,
        'timeslots': timeslots
    }
    return render(request, 'booking/booking.html', context)


def get_table(date, table_size, time):
    bookings = Booking.objects.all()
    tables = Table.objects.filter(category=table_size)
    tables_list = []
    for item in tables:
        tables_list.append(item.pk)
    date_bookings = Booking.objects.filter(date=date)
    if date_bookings.__len__() > 0:
        for booking in bookings:
            if time == booking.timeslot:
                if table_size == booking.table.category:
                    tables_list.remove(booking.table.pk)
    if len(tables_list) == 0:
        return 0
    else:
        return tables_list[0]
