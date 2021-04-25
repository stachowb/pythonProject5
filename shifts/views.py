from django.shortcuts import render
from django.views import View
from django.views.generic import DeleteView, DetailView
from .models import Shift
from django.http import HttpResponse
from django import forms
from .forms import ShiftForm


class HomePage(View):
    def get(self, request):
        return render(request, "basic.html")


class ShiftsList(View):

