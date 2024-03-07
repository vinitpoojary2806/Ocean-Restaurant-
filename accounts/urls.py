from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import path, include

urlpatterns = [
    path('register', views.registerUsers, name="RegisterUsers"),
    path('login', views.loginUsers, name="loginUsers"),
    path('logout', views.logoutUsers, name="logoutUsers")

]