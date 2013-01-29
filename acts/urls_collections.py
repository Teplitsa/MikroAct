# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDetailView

urlpatterns = patterns('',
    url(r'^$', CollectionListView.as_view(), name='collection_list'),
    url(r'^add/$', CollectionCreateView.as_view(), name='collection_add'),
    url(r'(?P<slug>[-_\w]+)/edit/$', CollectionUpdateView.as_view(), name='collection_edit'),
    url(r'(?P<slug>[-_\w]+)$', CollectionDetailView.as_view(), name='collection_detail'),
)
