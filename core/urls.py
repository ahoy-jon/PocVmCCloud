from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gate.core.views',
    url(r'^$', 'home'),
    url(r'^tests/$', 'home_tests'),
)
