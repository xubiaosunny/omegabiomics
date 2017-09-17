from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^company/$', company),
    url(r'^team/$', team),
    url(r'^news/$', news),
    url(r'^news/(?P<id>\d+)/$', news_detial),
    url(r'^partner/$', partner),
    url(r'^contact_us/$', contact_us),
]