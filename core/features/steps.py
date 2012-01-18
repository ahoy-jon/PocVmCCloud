from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    c = Client()
    response = c.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see content div')
def see_header(step):
    assert_equals(1, len(world.dom.cssselect('#content')))
    

