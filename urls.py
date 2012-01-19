from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'gate.views.home', name='home'),
    url(r'^', include('gate.core.urls')),
    url(r'^api/installed-apps/', include('gate.home.urls')),
    url(r'^api/market/', include('gate.market.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
