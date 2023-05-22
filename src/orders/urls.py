from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('history/', views.OrderListView.as_view(), name='history'),
]
