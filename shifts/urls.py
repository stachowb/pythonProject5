from django.urls import path
from .views import ShiftList, ShiftAdd

urlpatterns = [
    path('shifts/shift-list/', ShiftList.as_view(), name="shift-list"),
    path('shifts/add-shift/', ShiftAdd.as_view(), name="shift-add")
]
