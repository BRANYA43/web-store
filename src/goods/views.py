from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic

from .models import Good


class GoodListView(generic.ListView):
    model = Good
    template_name = 'goods/list.html'
    context_object_name = 'goods'
    paginate_by = 1

    def get_queryset(self):
        return self.model.objects.filter(is_show=True, category__title=self.kwargs['category'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = self.kwargs['category']
        return context
