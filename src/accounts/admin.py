from django.contrib import admin
from django.contrib.auth import get_user_model

from carts.admin import CartInline


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    exclude = ('password',)
    fieldsets = (
        ('Personal info', {'fields': ('username', 'email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined', 'is_active')
    inlines = (CartInline, )

