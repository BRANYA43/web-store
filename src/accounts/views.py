from django.contrib.auth import views as auth_views
from django.shortcuts import render


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(auth_views.LogoutView):
    ...
