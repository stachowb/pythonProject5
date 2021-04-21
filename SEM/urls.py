from django.contrib import admin
from django.urls import path
from shifts.views import (HomePage, ShiftView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('shift/<int:pk>', ShiftView.as_view(), name="shift_view")
]
