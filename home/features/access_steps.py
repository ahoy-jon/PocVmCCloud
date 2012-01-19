from lettuce import *
import simplejson

from django.test.client import Client
from nose.tools import assert_equals

from home.models import InstalledApp as App

@before.all
def set_browser():
    world.browser = Client()

    for app in App.objects.all():
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

@step(u'I delete first app')
def given_i_delete_first_app(step):
    response = world.browser.delete("/api/installed-apps/hello-world-01/")

@step(u'Given I send an app for installation')
def given_i_send_an_app_for_installation(step):
    response = world.browser.post("/api/installed-apps/",
            content_type="application/json",
            data='{"name":"Hello World 01", "slug":"hello-world-01"}')
    assert_equals(201, response.status_code)

@after.all
def delete_all(total):
    for app in App.objects.all():
        app.delete()
