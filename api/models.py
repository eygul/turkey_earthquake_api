from django.db import models

class Quake(models.Model):
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    depth = models.CharField(max_length=200)
    md = models.CharField(max_length=200)
    ml = models.CharField(max_length=200)
    mw = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location