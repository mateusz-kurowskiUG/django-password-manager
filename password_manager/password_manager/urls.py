from django.contrib import admin
from django.urls import path, include
from registration import views as register_views
from django.contrib.auth.views import LoginView,LogoutView

from django.conf.urls.static import static
from django.conf import settings

"""
URL configuration for password_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("passwd_manager_app.urls")),
    path('', include("django.contrib.auth.urls")),
    path('register/',register_views.register,name="Register" ),
    path('login/',LoginView.as_view(),name="Login" ),
    path('logout/',LogoutView.as_view(),name="Logout" ),
    path('signed_out/',LogoutView.as_view(),name="Logout" ),    
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)