from django.shortcuts import render
from .models import *
# Create your views here.


def job(request):
    item = Job.objects.all()
    for i in range(len(item)):
        item[i].duty = item[i].duty.replace('\r\n', '<br>')
        item[i].request = item[i].request.replace('\r\n', '<br>')
    return render(request, 'job/job.html', {'item': item})