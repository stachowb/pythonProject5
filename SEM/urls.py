from django.contrib import admin
from django.urls import path, include
from shifts.views import HomePage, ShiftList, ShiftAdd

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('shifts/', include("shifts.urls")),
]
