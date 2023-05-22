from django import template

register = template.Library()


@register.filter
def order_by(queryset, arg):
    return queryset.order_by(arg)
