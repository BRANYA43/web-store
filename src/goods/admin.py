from django.contrib import admin

from .forms import OrderedCategoryAndSubCatalogFormset, OrderedCatalogForm
from .models import Category, SubCatalog, Catalog, Good


class GoodInline(admin.TabularInline):
    model = Good
    fields = ('title', 'slug', 'quantity', 'price', 'is_show')
    prepopulated_fields = {'slug': ('title',)}
    extra = 0
    show_change_link = True


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'quantity', 'price', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_show', 'category')
    readonly_fields = ('created', 'updated')


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
    inlines = (GoodInline,)


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    inlines = (CategoryInline,)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_num')
    inlines = (SubCatalogInline, CategoryInline)
    form = OrderedCatalogForm
