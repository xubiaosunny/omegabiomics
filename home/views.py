from django.shortcuts import render
from home.models import *
from job.models import *
from medicine.models import *
from service.models import *
from support.models import *
from about.models import *
from django.db.models import Q
from itertools import chain
# Create your views here.

def index(request):
    carousel = Carousel.objects.filter(display=True)
    company = Company.objects.first()
    return render(request, 'home/index.html', {'carousel': carousel, 'company': company})


def search(request):
    query = request.GET.get("query")
    result = {
        '科技服务': ThirdItem.objects.filter(name__icontains=query),
        '医学健康': Medicine.objects.filter(name__icontains=query),
        '技术支持': Support.objects.filter(name__icontains=query),
        '新闻动态': News.objects.filter(name__icontains=query),
    } if query else None
    return render(request, 'home/search.html', {'result': result})



