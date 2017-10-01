try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object
import collections

from service.models import *
from support.models import *
from medicine.models import *
from home.models import *


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        item = FristItem.objects.all()
        service = collections.OrderedDict()
        for i in item:
            service[i.name] = [('/service/%d/' % x.id, x.name) for x in i.seconditem_set.all()]
        request.session['service'] = service
        request.session['medicine'] = [('/medicine/%d/' % x.id, x.name) for x in Medicine.objects.all()]
        request.session['support'] = [('/support/%d/' % x.id, x.name) for x in Support.objects.all()]
        request.session['keyword'] = [x.name for x in Keyword.objects.all()]
        return None