# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^collective/$', 'acts.views.home', name='home'),
)	
