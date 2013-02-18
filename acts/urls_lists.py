# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns,  url

from .views import ListListView, ListCreateView, ListUpdateView, ListFollowView, ListDetailView

urlpatterns = patterns('',
    url(r'^$', ListListView.as_view(), name='list_list'),
    url(r'^add/$', ListCreateView.as_view(), name='list_add'),
    url(r'(?P<slug>[-_\w]+)/edit/$', ListUpdateView.as_view(), name='list_edit'),
    url(r'(?P<slug>[-_\w]+)/follow/$', ListFollowView.as_view(), name='list_follow'),
    url(r'(?P<slug>[-_\w]+)$', ListDetailView.as_view(), name='list_detail'),
)
