from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$',support_item),
]