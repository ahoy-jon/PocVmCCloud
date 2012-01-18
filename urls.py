from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'gate.views.home', name='home'),
    url(r'^', include('gate.core.urls')),
    url(r'^api/installed-apps', include('gate.home.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': "/home/gelnior/projets/mycloud/gate/static", 
    #    'show_indexes': True}),
)
urlpatterns += staticfiles_urlpatterns()
