from django.conf.urls.defaults import patterns, url

from gate.market.views import AppsResource

urlpatterns = patterns('market.views',
    url(r'^apps/$', AppsResource()),
)
