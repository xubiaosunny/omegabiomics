from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$',service_item),
    url(r'^$',service_index),
]