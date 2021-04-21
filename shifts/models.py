from django.db import models


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

    @property
    def shift_length(self):
        return self.clock_out_date - self.clock_in_date


