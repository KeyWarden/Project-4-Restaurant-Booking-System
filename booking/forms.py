from django import forms
from .models import Booking
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
#        user = user
        fields = ['date', 'table', 'timeslot']