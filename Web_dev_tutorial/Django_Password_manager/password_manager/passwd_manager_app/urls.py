from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("home/", views.home, name="Home"),
    path("passwords/", views.passwords, name="My Passwords"),
    path("add_new/", views.add_new, name="Add new"),
    path("<int:id>", views.passwords, name="My Passwords2"),
    ]

