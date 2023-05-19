from django import forms
from django.forms import modelformset_factory

from carts.models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('cart', 'good', 'quantity')
        widgets = {
            'cart': forms.HiddenInput,
            'good': forms.HiddenInput,
        }


CartItemFormSet = modelformset_factory(CartItem, CartItemForm, extra=0)
