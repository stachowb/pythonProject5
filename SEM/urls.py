from django.contrib import admin
from django.urls import path
from SEM.shifts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="home")
]
