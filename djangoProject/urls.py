
from django.contrib import admin
from django.urls import path
from . import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage.homePage, name='index')
]
