# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns,  url

from .views import CampaignListView, CampaignCreateView, CampaignUpdateView, CampaignFollowView, CampaignDetailView

urlpatterns = patterns('',
    url(r'^$', CampaignListView.as_view(), name='campaign_list'),
    url(r'^add/$', CampaignCreateView.as_view(), name='campaign_add'),
    url(r'(?P<slug>[-_\w]+)/edit/$', CampaignUpdateView.as_view(), name='campaign_edit'),
    url(r'(?P<slug>[-_\w]+)/follow/$', CampaignFollowView.as_view(), name='campaign_follow'),
    url(r'(?P<slug>[-_\w]+)$', CampaignDetailView.as_view(), name='campaign_detail'),
)
