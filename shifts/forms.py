from django import forms
from .models import Shift


class AddShiftForm(forms.Form):
    driver_name = forms.CharField(max_length=60, label="Driver Name")
    company_name = forms.CharField(max_length=60, label="Company Name")
    eq_type = forms.CharField(max_length=60, label="Equipment Type")
    clock_in_date = forms.CharField(max_length=60, label="Clock In")
    clock_out_date = forms.CharField(max_length=60, label="Clock Out")
    km_driven = forms.IntegerField(label="Kilometers")


class AddFileForm(forms.Form):
    file = forms.FileField()
