from django.shortcuts import render
from django.views import View
from django.views.generic import DeleteView, DetailView
from .models import Shift
from django.http import HttpResponse
from django import forms
from .forms import ShiftForm



def shift_create(request):
    form = ShiftForm(request.POST or None)
    if form.is_valid():
        form.save()

    ctx = {'form': form}
    return render(request, "shift_create.html", ctx )


# class HomePage(View):
#     def get(self, request):
#         shifts = Shift.objects.all()
#         return render(request, "homepage.html", {"form": form})

    def post(self, request):
        driver_name = request.POST.get('driver_name')
        company_name = request.POST.get('company_name')
        eq_type = request.POST.get('eq_type')
        clock_in = request.POST.get('clock_in')
        clock_out = request.POST.get('clock_out')
        km_driven = int(request.POST.get('km_driven'))
        Shift.objects.create(driver_name=driver_name, company_name=company_name, eq_type=eq_type, clock_in_date=clock_in,
                             clock_out_date=clock_out, km_driven=km_driven)

        return HttpResponse("record added")


class FileView(View):
    pass
