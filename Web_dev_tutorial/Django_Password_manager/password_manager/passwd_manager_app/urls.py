from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("home/", views.home, name="Home"),
    path("passwords/", views.passwords, name="My Passwords"),
    path("add_new/", views.add_new, name="Add new"),
    path("<int:id>/", views.my_password, name="My Password"),
    path("signed_out/", views.signed_out, name="Signed_out"),
    path("@<str:username>/", views.my_account, name="My account"),
    path("contact/", views.contact, name="Contact"),
    ]