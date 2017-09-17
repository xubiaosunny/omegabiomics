from django.shortcuts import render
from home.models import *
# Create your views here.

def index(request):
    carousel = Carousel.objects.filter(display=True)
    company = Company.objects.first()
    return render(request, 'home/index.html', {'carousel': carousel, 'company': company})
