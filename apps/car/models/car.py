from django.contrib.gis.db import models
from .owner import Owner


class Car(models.Model):

    car_type = (
        ("s", "small"),
        ("b", "big")
    )

    type = models.CharField(choices=car_type, default="s")
    color = models.CharField(max_length=50, help_text="Enter the car color")
    length = models.FloatField(verbose_name="car`s length")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cars')
    load_volume = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type == 'b':
            big_car_exists = Car.objects.filter(owner=self.owner, type='b').exists()
            if big_car_exists and not self.pk:
                raise Exception("Each driver can only have one heavy vehicle.")

        super().save(*args, **kwargs)


class Positioning(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='positions')
    location = models.PointField()
    date = models.DateTimeField(auto_now_add=True)

