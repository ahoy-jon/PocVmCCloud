from django.conf.urls.defaults import patterns, url

from gate.home.views import InstalledAppsResource, InstalledAppResource

urlpatterns = patterns('',
    url(r'^$', InstalledAppsResource()),
    url(r'^(?P<slug>[a-z0-9-]+)/$', InstalledAppResource()),
)
