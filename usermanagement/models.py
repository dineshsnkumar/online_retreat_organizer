from django.db import models

# Create your models here.
class Retreat(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField("start_date")
    end_date = models.DateTimeField("end_date")
    description = models.CharField(max_length=1200, blank= True)
    schedule = models.TextField(blank=True)
    zoom_link = models.URLField(blank=True)
    retreat_image = models.URLField(default="https://vh1220.z2systems.com/neon/resource/vh1220/images/buddhalei3(2).JPG")
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200, blank= True)
    def __str__(self):
        return self.name


