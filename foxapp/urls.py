"""foxapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from custom_auth import views as custom_auth
from user_profile import views as profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', custom_auth.register_page, name='register'),
    path('login/', custom_auth.LoginPageView.as_view(), name='login'),
    path('logout/', custom_auth.logout_user, name='logout'),
    path('profile/', profile.profile_page, name='profile')
]
