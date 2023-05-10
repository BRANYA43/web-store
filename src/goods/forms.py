from django import forms
from django.core.exceptions import ValidationError

from .models import Catalog


def clean_order_nums(order_nums):
    try:
        order_nums.index(0)
        raise ValidationError('Order num must not be 0')
    except ValueError:
        pass

    for i in range(1, len(order_nums) + 1):
        try:
            index = order_nums.index(i)
        except ValueError:
            if i == 1:
                raise ValidationError('Order num must start of one.')
            raise ValidationError(f'Order num must be ascending order on one.  Last order num is {i - 1}.')
        del order_nums[index]


class OrderedCatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'

    def clean(self):
        super().clean()
        order_num = self.cleaned_data['order_num']
        order_nums = [catalog.order_num for catalog in Catalog.objects.exclude(pk=self.instance.pk).exclude(order_num__isnull=True)]
        if order_num:
            order_nums.append(order_num)
        if order_nums:
            clean_order_nums(order_nums)


class OrderedCategoryAndSubCatalogFormset(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        order_nums = [form.instance.order_num for form in self.forms if form.instance.order_num is not None]
        if order_nums:
            clean_order_nums(order_nums)
