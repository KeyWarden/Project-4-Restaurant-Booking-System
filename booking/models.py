from django.db import models

# Create your models here.


class Tables(models.Model()):
    size = models.IntegerField()
    category = models.CharField()
    upper_limit = models.IntegerField()


class Timeslot(models.Model()):
    time = models.TimeField()