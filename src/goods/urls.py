from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('<str:category>/list/', views.GoodListView.as_view(), name='good_list'),
]
