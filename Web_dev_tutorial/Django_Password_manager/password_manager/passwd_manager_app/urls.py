from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("passwords/", views.passwords, name="My Passwords"),
    ]

