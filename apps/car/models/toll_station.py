from django.contrib.gis.db import models


class TollStation(models.Model):
    name = models.CharField(max_length=25)
    toll_per_station = models.PositiveIntegerField()
    location = models.PointField()


class Road(models.Model):
    name = models.CharField(max_length=50)
    width = models.FloatField()
    geom = models.MultiLineStringField()
