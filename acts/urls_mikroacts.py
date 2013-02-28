# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import MikroActListView, MikroActCreateView, MikroActUpdateView, \
        MikroActDeleteView, MikroActDetailView

urlpatterns = patterns('',
    url(r'^$', MikroActListView.as_view(), name='mikroact_list'),
    url(r'^add/$', MikroActCreateView.as_view(), name='mikroact_add'),
    url(r'(?P<slug>[-_\w]+)/edit/$', MikroActUpdateView.as_view(), name='mikroact_edit'),
    url(r'(?P<slug>[-_\w]+)/delete/$', MikroActDeleteView.as_view(), name='mikroact_delete'),
    url(r'(?P<slug>[-_\w]+)$', MikroActDetailView.as_view(), name='mikroact_detail'),
)
