from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('history/', views.OrderListView.as_view(), name='history'),
    path('checkout/', views.checkout_order, name='checkout'),
    path('<str:uuid>/detail/', views.OrderDetailView.as_view(), name='detail'),
]
