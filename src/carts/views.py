from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from carts.forms import CartItemFormSet
from carts.models import CartItem


class CartView(LoginRequiredMixin, generic.ListView):
    model = CartItem
    template_name = 'carts/item_list.html'
    context_object_name = 'items'
    formset = CartItemFormSet

    def get_queryset(self):
        return self.model.objects.filter(cart=self.request.user.cart)

