from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView, DetailView
from .models import Shift
from django.http import HttpResponse, Http404
from .forms import AddShiftForm, AddFileForm
from django.contrib import messages


class HomePage(View):
    def get(self, request):
        form = AddFileForm(request.POST, request.FILES)
        return render(request, "basic.html", {"form": form})


class ShiftList(View):
    def get(self, request):
        shifts = Shift.objects.all()
        return render(request, "shift_list.html", {"shifts": shifts})


class ShiftAdd(View):
    def get(self, request):
        form = AddShiftForm()
        models = 
        return render(request, "shift_add.html", {"form": form})

    def post(self, request):
        form = AddShiftForm(request.POST)
        if form.is_valid():
            try:
                driver_name = form.cleaned_data['driver_name']
                company_name = form.cleaned_data["company_name"]
                eq_type = form.cleaned_data["eq_type"]
                clock_in_date = form.cleaned_data["clock_in_date"]
                clock_out_date = form.cleaned_data["clock_out_date"]
                km_driven = form.cleaned_data["km_driven"]
                shift = Shift.objects.create(driver_name=driver_name, company_name=company_name, eq_type=eq_type,
                                             clock_in_date=clock_in_date, clock_out_date=clock_out_date,
                                             km_driven=km_driven)
                shift.save()
            except Exception:
                messages.error(request, "Error when adding new shift")
                return redirect("shift-add")
            else:
                messages.success(request, 'Shift added successfully')
                return redirect("shift-list")
        return HttpResponse("Error adding shift")
