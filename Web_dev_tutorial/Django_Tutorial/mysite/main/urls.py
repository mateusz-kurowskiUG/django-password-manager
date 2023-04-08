from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="Index"),
    path("", views.home, name="Home"),
    path("/", views.home, name="Home"),
]
