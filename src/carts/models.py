from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from goods.models import Good


class Cart(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user.username

    def get_total(self):
        return sum(item.get_total() for item in self.items.all())

    def get_quantity(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.good.title

    def get_total(self):
        return self.good.price * self.quantity


@receiver(post_save, sender=get_user_model())
def create_cart(sender, **kwargs):
    if kwargs.get('created'):
        cart = Cart.objects.create(user=kwargs.get('instance'))
        cart.save()
