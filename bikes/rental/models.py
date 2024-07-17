from django.db import models


class Bikes(models.Model):
    bike_name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    quantity = models.IntegerField(blank=False, verbose_name='Quantity')

    def __str__(self):
        return self.bike_name