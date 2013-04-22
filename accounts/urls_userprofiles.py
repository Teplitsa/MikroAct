# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf.urls import patterns, include, url

from .views import UserRegisterView, UserRegisterCompleteView, UserUpdateView, UserDetailView, UserListView

urlpatterns = patterns('django.contrib.auth.views',
    url(r'login/$', 'login', {'template_name': 'accounts/login.html'}, name='user_login'), 
    url(r'logout/$', 'logout', {'template_name': 'accounts/logout.html'}, name='user_logout'), 
    url(r'^password_reset/$', 'password_reset', name='user_password_reset'),
    url(r'^password_reset/done/$', 'password_reset_done', name='user_password_reset_done'),
    url(r'^password_reset/confirm/$', 'password_reset_done', name='user_password_reset_done'),
    url(r'^password_reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'password_reset_confirm', name='user_password_reset_confirm'),
    url(r'^password_reset/complete/$', 'password_reset_complete',
        name='user_password_reset_complete')

)

urlpatterns += patterns('',
    url(r'register/$', UserRegisterView.as_view(), name='user_register'), 
    url(r'^$', UserListView.as_view(), name='user_list'),
    url(r'register/done/$', UserRegisterCompleteView.as_view(), name='user_register_done'), 
    url(r'(?P<username>[-_\w]+)/edit/$', UserUpdateView.as_view(), name='user_edit'),
    url(r'(?P<username>[-_\w]+)/$', UserDetailView.as_view(), name='user_detail'),
)
