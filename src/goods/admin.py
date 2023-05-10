from django.contrib import admin

from .forms import OrderedCategoryAndSubCatalogFormset, OrderedCatalogForm
from .models import Category, SubCatalog, Catalog


class CategoryInline(admin.TabularInline):
    model = Category
    fields = ('title', 'order_num')
    extra = 0
    show_change_link = True
    formset = OrderedCategoryAndSubCatalogFormset


class SubCatalogInline(admin.TabularInline):
    model = SubCatalog
    fields = ('title', 'order_num')
    extra = 0
    show_change_link = True
    formset = OrderedCategoryAndSubCatalogFormset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'sub_catalog')


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    inlines = (CategoryInline,)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_num')
    inlines = (SubCatalogInline, CategoryInline)
    form = OrderedCatalogForm
