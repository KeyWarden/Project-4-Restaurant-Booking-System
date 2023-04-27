from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tables(models.Model):
    size = models.IntegerField(null=False, blank=False)
    category = models.CharField(max_length=10, null=False, blank=False)
    upper_limit = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.category + str(self.pk)


class Timeslot(models.Model):
    time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return str(self.time)


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking"
    )
    date = models.DateField(null=False, blank=False)
    number_of_people = models.IntegerField(null=False, blank=False)
    table = models.ForeignKey(
        Tables, on_delete=models.CASCADE, related_name="booking"
    )
    timeslot = models.ForeignKey(
        Timeslot, on_delete=models.CASCADE, related_name="booking"
    )

    def __str__(self):
        return (
            str(self.user) + " " + str(self.date) + " " + str(self.table) +
            " " + str(self.timeslot)
            )

    class Meta:
        ordering = ['date']
