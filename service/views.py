from django.shortcuts import render
from .models import *
# Create your views here.


def service_index(request):
    try:
        description = ServiceIndex.objects.first().description
    except:
        description = ''
    return render(request, 'service/service_index.html', {'description': description})


def service_item(request, id):
    item = SecondItem.objects.get(id=id)
    items = item.thirditem_set.all()
    return render(request, 'service/service.html', {'items': items})


