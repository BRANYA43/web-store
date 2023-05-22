from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('add/<str:good>/', views.add_cart_item, name='add_item'),
    path('', views.CartView.as_view(), name='cart'),
]
