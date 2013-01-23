# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import CollectionListView, CollectionDetailView

urlpatterns = patterns('',
    url(r'^$', CollectionListView.as_view(), name='collection_list'),
    url(r'(?P<slug>[-_\w]+)$', CollectionDetailView.as_view(), name='collection_detail'),
)
