from django.db import models

# Create your models here.
class Retreat(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField("start_date")
    end_date = models.DateTimeField("end_date")
    description = models.CharField(max_length=1200, blank= True)