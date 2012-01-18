from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home.views',
    url(r'^/$', 'installed_apps'),
)
