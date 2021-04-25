from django.contrib import admin
from django.urls import path
from shifts.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
]
