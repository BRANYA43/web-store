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
    sub_catalog = models.ForeignKey(to=SubCatalog, on_delete=models.SET_NULL, related_name='categories', null=True, blank=True)
    order_num = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('title', 'catalog__title', 'sub_catalog')

    def __str__(self):
        return self.title
