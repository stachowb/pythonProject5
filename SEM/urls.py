from django.contrib import admin
from django.urls import path
from shifts.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]
