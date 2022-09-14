from django.shortcuts import render
from katalog.models import CatalogItem


# TODO: Create your views here.
def show_catalog(request):
    data = CatalogItem.objects.all()
    context = {
        'list_barang': data,
        'nama': 'Nadhira Shahnaz Zain',
        'npm' : '2106701186'
    }
    return render(request, "katalog.html", context)
