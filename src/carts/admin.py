from django.contrib import admin

from carts.models import Cart, CartItem


class CartInline(admin.StackedInline):
    model = Cart
    fields = ('quantity', 'total')
    readonly_fields = ('quantity', 'total')
    show_change_link = True

    def quantity(self, instance):
        return instance.get_quantity()

    def total(self, instance):
        return instance.get_total()


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ('good', 'quantity', 'price', 'total')
    readonly_fields = ('good', 'quantity', 'price', 'total')
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def good(self, instance):
        return instance.good.title

    def quantity(self, instance):
        return instance.quantity

    def price(self, instance):
        return instance.good.price

    def total(self, instance):
        return instance.get_total()


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInline,)
    readonly_fields = ('user',)
