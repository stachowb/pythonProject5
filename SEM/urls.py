from django.contrib import admin
from django.urls import path, include
from shifts.views import HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('shifts/', include("shifts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_URL)

