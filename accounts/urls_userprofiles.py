# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import UserRegisterView, UserRegisterCompleteView, UserUpdateView, UserDetailView

urlpatterns = patterns('django.contrib.auth.views',
    url(r'login/$', 'login', {'template_name': 'accounts/login.html'}, name='user_login'), 
    url(r'logout/$', 'logout', {'template_name': 'accounts/logout.html'}, name='user_logout'), 
    url(r'^password_reset/$', 'password_reset', name='user_password_reset')
)

urlpatterns += patterns('',
    url(r'register/$', UserRegisterView.as_view(), name='user_register'), 
    url(r'register/done/$', UserRegisterCompleteView.as_view(), name='user_register_done'), 
    url(r'(?P<username>[-_\w]+)/edit/$', UserUpdateView.as_view(), name='user_edit'),
    url(r'(?P<username>[-_\w]+)/$', UserDetailView.as_view(), name='user_detail'),
)
