import simplejson

from django.test.client import Client
from lettuce import step, before, after
from nose.tools import assert_equals

from home.models import InstalledApp
from market.models import App

@before.all
def set_browser():
    world.browser = Client()

    for app in App.objects.all():
        app.delete()

    for app in InstalledApp.objects.all():
        app.delete()      

    app = App(name="Hello World 01", slug="hello-world-01")
    app.save()
    app = App(name="Hello World 02", slug="hello-world-02")
    app.save()

    

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.apps = simplejson.loads(response.content)

@step(r'I see (\d) apps at JSON format')
def see_apps(step, nb_app):
    assert_equals(int(nb_app), len(world.apps["rows"]))


