from django.contrib import admin
from django.urls import path
from shifts.views import shift_create

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomePage.as_view(), name="home"),
    path('', shift_create)
]
