from django.shortcuts import render
from .models import *
# Create your views here.

def support_item(request, id):
    item = Support.objects.get(id=id)
    return render(request, 'support/support.html', {'item': item})

