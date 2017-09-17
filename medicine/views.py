from django.shortcuts import render
from .models import *
# Create your views here.


def medicine_item(request, id):
    item = Medicine.objects.get(id=id)
    return render(request, 'medicine/medicine.html', {'item': item})
