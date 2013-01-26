# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

urlpatterns = patterns('django.contrib.auth.views',
    url(r'login/$', 'login', {'template_name': 'accounts/login.html'}), 
    url(r'^password_reset/$', 'password_reset', name='auth_password_reset')
)
