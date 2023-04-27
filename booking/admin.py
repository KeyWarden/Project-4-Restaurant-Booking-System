from django.contrib import admin
from .models import Tables
from .models import Timeslot
from .models import Booking

# Register your models here.
admin.site.register(Tables)
admin.site.register(Timeslot)
admin.site.register(Booking)