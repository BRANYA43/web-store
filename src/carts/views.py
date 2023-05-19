from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_GET

from carts.forms import CartItemFormSet
from carts.models import CartItem
from goods.models import Good


@login_required
@require_GET
def add_cart_item(request, *args, **kwargs):
    cart = request.user.cart
    good = Good.objects.get(slug=kwargs['good'])
    item = CartItem.objects.create(cart=cart, good=good)
    item.save()
    return redirect(reverse_lazy('carts:cart'))


class CartView(LoginRequiredMixin, generic.ListView):
    model = CartItem
    template_name = 'carts/item_list.html'
    context_object_name = 'items'
    formset = CartItemFormSet

    def get_queryset(self):
        return self.model.objects.filter(cart=self.request.user.cart)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['formset'] = self.formset(queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        formset = self.formset(request.POST)
        if formset.is_valid():
            formset.save()
        return redirect(reverse_lazy('carts:cart'))

