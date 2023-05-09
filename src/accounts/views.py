from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import UserRegisterForm, UserContinueRegisterForm


class ContinueRegisterView(generic.UpdateView):
    model = get_user_model()
    template_name = 'accounts/register/continue_form.html'
    form_class = UserContinueRegisterForm
    success_url = reverse_lazy('accounts:login')


class RegisterView(generic.CreateView):
    model = get_user_model()
    template_name = 'accounts/register/form.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy('accounts:continue_register', kwargs={'pk': self.object.pk})


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(auth_views.LogoutView):
    ...
