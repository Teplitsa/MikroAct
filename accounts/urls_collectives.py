# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import CollectiveDetailView

urlpatterns = patterns('',
    url(r'(?P<slug>[-_\w]+)$', CollectiveDetailView.as_view(), name='collective_detail'),
)
