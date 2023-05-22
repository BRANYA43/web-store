from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_GET

from orders.models import Order, OrderItem


@login_required
@require_GET
def checkout_order(request, *args, **kwargs):
    cart = request.user.cart
    order = Order.objects.create(user=request.user)
    order.save()
    print(order)
    for cart_item in cart.items.all():
        order_item = OrderItem.objects.create(
            order=order,
            title=cart_item.good.title,
            slug=cart_item.good.slug,
            quantity=cart_item.quantity,
            price=cart_item.good.price
        )
        order_item.save()
        cart_item.delete()
    return redirect(reverse_lazy('orders:history'))


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
