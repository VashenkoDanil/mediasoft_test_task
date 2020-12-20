from django.db import models

from address.models import Address


class Shops(models.Model):
    name = models.CharField(max_length=256)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    time_open = models.TimeField()
    time_close = models.TimeField()

    def __str__(self):
        return self.name
