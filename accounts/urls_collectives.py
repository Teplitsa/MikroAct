# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import CollectiveListView, CollectiveCreateView, \
        CollectiveUpdateView, CollectiveDetailView, CollectiveJoinView, \
        CollectiveFollowView, CollectiveUnFollowView

urlpatterns = patterns('',
    url(r'^$', CollectiveListView.as_view(), name='collective_list'),
    url(r'^add/$', CollectiveCreateView.as_view(), name='collective_add'),
    url(r'(?P<slug>[-_\w]+)/edit/$', CollectiveUpdateView.as_view(), name='collective_edit'),
    url(r'(?P<slug>[-_\w]+)/follow/$', CollectiveFollowView.as_view(), name='collective_follow'),
    url(r'(?P<slug>[-_\w]+)/unfollow/$', CollectiveUnFollowView.as_view(), name='collective_unfollow'),
    url(r'(?P<slug>[-_\w]+)/join/$', CollectiveJoinView.as_view(), name='collective_join'),
    url(r'(?P<slug>[-_\w]+)/$', CollectiveDetailView.as_view(), name='collective_detail'),
)
