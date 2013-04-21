# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mikroact.views.home', name='home'),
    url(r'^collective/', include('accounts.urls_collectives')),
    url(r'^campaign/', include('acts.urls_campaigns')),
    url(r'^act/', include('acts.urls_mikroacts')),

    url(r'^user/', include('accounts.urls_userprofiles')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^comments/', include('fluent_comments.urls')),
)
