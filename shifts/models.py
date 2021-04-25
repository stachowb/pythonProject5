from django.db import models
from datetime import datetime

class Shift(models.Model):
    driver_name = models.CharField(max_length=60)
    company_name = models.CharField(max_length=60)

    EQ_TYPES = (
        (1, "Trekker"),
        (2, "Containerbil m/løftelem"),
        (3, "Containerbil"),
        (4, "-")
    )
    eq_type = models.CharField(max_length=60, choices=EQ_TYPES)
    clock_in_date = models.DateTimeField(max_length=60)
    clock_out_date = models.DateTimeField(max_length=60)
    km_driven = models.IntegerField(default=0)

    def shift_length(self):
        frt = '%d-%m-%Y %H:%M'

        clock_in = datetime.strptime(self.clock_in_date, frt)
        clock_out = datetime.strptime(self.clock_out_date, frt)

        return clock_out - clock_in

    def save(self, *args, **kwargs):
        self.shift_length = self.shift_length()

        super(Shift, self).save(*args, **kwargs)



