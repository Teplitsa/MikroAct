from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mikroact.views.home', name='home'),
    # url(r'^mikroact/', include('mikroact.foo.urls')),

    (r'^accounts/', include('userena.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
