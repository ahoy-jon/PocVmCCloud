from lettuce import *
import simplejson

from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.apps = simplejson.loads(response.content)

@step(r'I see two apps at JSON format')
def see_apps(step):
    assert 2 == len(world.apps)


