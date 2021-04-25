from django.contrib import admin
from django.urls import path
from shifts.views import HomePage, ShiftList, ShiftAdd

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('shifts/shift-list/', ShiftList.as_view(), name="shift-list"),
    path('shifts/add-shift/', ShiftAdd.as_view(), name="shift-add")
]
