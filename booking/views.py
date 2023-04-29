from django.shortcuts import render, redirect
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
#        date = request.POST.get('date_name')
#        table_size = request.POST.get('size_name')
#        time = request.POST.get('time_name')
#        timeslots = Timeslot.objects.filter(time=time)
#        timeslots_list = []
#        for instance in timeslots:
#            timeslots_list.append(instance)
#        timeslot = timeslots_list[0]
#        table_id = get_table(date, table_size, timeslot)
#        user = request.user
#        if table_id != 0:
#            table = Table.objects.get(pk=table_id)
#            Booking.objects.create(
#                user=user, date=date, table=table, timeslot=timeslot
#                )
#
#            return redirect('Home')
#        elif table_id == 0:
#            return redirect('Make Booking')
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
    return render(request, 'booking/edit_booking.html')
