from .models import Catalog


def catalogs(request):
    queryset = Catalog.objects.order_by('title')
    return {'catalogs': queryset}
