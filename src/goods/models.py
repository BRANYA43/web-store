from django.db import models

from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    order_num = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class SubCatalog(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    parent = models.ForeignKey(to=Catalog, on_delete=models.SET_NULL, related_name='subs', null=True, blank=True)
    order_num = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('title', 'parent__title')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    catalog = models.ForeignKey(to=Catalog, on_delete=models.SET_NULL, related_name='categories', null=True, blank=True)
    sub_catalog = models.ForeignKey(to=SubCatalog, on_delete=models.SET_NULL, related_name='categories', null=True,
                                    blank=True)
    order_num = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('title', 'catalog__title', 'sub_catalog')

    def __str__(self):
        return self.title


class Good(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, related_name='goods', null=True, blank=True)
    image = models.ImageField(upload_to='goods/', default='../no-image.png')
    short_description = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', 'category__title')

    def __str__(self):
        return self.title