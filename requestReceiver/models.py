from django.db import models

# Create your models here.

class AirQuality(models.Model):
    dateTime = models.CharField(max_length=100)
    AQ = models.IntegerField()
    CO2 = models.IntegerField()
    