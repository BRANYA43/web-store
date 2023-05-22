from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('title', 'slug', 'quantity', 'price', 'total')
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def total(self, instance):
        return instance.get_total()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'is_paid', 'created')
    readonly_fields = ('uuid', 'user', 'is_paid', 'created')
    inlines = (OrderItemInline,)
