from django.urls import path
from .views import ShiftList, ShiftAdd

urlpatterns = [
    path('shift-list/', ShiftList.as_view(), name="shift-list"),
    path('add-shift/', ShiftAdd.as_view(), name="shift-add")
]
