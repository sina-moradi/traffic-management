from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    national_code = models.PositiveIntegerField()

    def __str__(self):
        return self.name
