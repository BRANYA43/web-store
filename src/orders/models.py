from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


class Order(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, db_index=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, related_name='orders')
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', '-is_paid')

    def __str__(self):
        return self.uuid


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('order__uuid', 'slug')

    def __str__(self):
        return self.title
