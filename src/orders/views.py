from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from orders.models import Order


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

