from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def company(request):
    item = Company.objects.first()
    return render(request, 'about/company.html', {'item': item})


def team(request):
    item = Team.objects.all()
    return render(request, 'about/team.html', {'item': item})


def news(request):
    item = News.objects.all()
    paginator = Paginator(item, 20)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    range_pages = paginator.page_range[0:paginator.num_pages]
    return render(request, 'about/news_index.html', {'contacts': contacts, 'pages': range_pages})


def news_detial(request, id):
    item = get_object_or_404(News, id=id)
    post =  News.objects.all()[:4]
    return render(request, 'about/news_detial.html', {'item': item, 'post': post})


def partner(request):
    item = Partner.objects.all()
    return render(request, 'about/partner.html', {'item': item})


def contact_us(request):
    return render(request, 'about/contact_us.html', {})