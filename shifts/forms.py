from django import forms
from .models import Shift

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            "driver_name",
            "company_name"
        ]