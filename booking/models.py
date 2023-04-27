from django.db import models

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