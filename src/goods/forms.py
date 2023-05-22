from django import forms
from django.core.exceptions import ValidationError

from .models import Catalog
from .utilities import clean_order_nums


class CategoryCatalogCheckForm(forms.ModelForm):
    def clean(self):
        super().clean()
        catalog = self.cleaned_data['catalog']
        sub_catalog = self.cleaned_data['sub_catalog']
        if catalog and sub_catalog:
            raise ValidationError('Category cannot be in the catalog and the sub catalog one time.')


class OrderedCatalogCheckForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'

    def clean(self):
        super().clean()
        order_num = self.cleaned_data['order_num']
        order_nums = [catalog.order_num for catalog in
                      Catalog.objects.exclude(pk=self.instance.pk).exclude(order_num__isnull=True)]
        if order_num:
            order_nums.append(order_num)
        if order_nums:
            clean_order_nums(order_nums)


class OrderedCheckFormset(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        order_nums = [form.instance.order_num for form in self.forms if form.instance.order_num is not None]
        if order_nums:
            clean_order_nums(order_nums)
