from django.shortcuts import render
from mywatchlist.models import myWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data = myWatchList.objects.all()
    context = {
        'list_film': data,
        'nama': 'Nadhira Shahnaz Zain',
        'npm': '2106701186'
    }
    return render(request, "mywatchlist.html", context)

    

def show_xml(request):
    data = myWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = myWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = myWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = myWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
