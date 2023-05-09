from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/continue/<int:pk>/', views.ContinueRegisterView.as_view(), name='continue_register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password/change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/done/', TemplateView.as_view(template_name='accounts/password/reset_done/'),
         name='password_reset_done'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password_reset'),
]

