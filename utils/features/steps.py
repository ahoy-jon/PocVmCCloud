# -*- coding: utf-8 -*-
from lettuce import step, world
from nose.tools import assert_equals
from gate.utils import config_files as utils

from settings import NGINX_CONF_FILE

from home.models import InstalledApp as App

TEST_FILE = "./utils/features/test"


@step(u'I have a test file open with (\d) lines')
def given_i_have_a_test_file_open_with_5_lines(step, nbline):
    file = open(TEST_FILE, "r")
    assert_equals(len(file.readlines()), int(nbline))
    file.close()

@step(u'When I delete line from 2 to 4')
def when_i_delete_line_from_2_to_4(step):
    utils.delete_lines(TEST_FILE, 2, 4)
    world.file = open(TEST_FILE, "r")

@step(u'Then The file contains (\d) lines')
def then_the_file_contains_3_lines(step, nbline):
    assert_equals(len(world.file.readlines()), int(nbline))
    world.file.close()

@step(u'Given I open test nginx configuration file')
def given_i_open_test_nginx_configuration_file(step):
    world.file = open(NGINX_CONF_FILE)

@step(u'I delete app list in configuration file')
def when_i_delete_app_list_in_configuration_file(step):
    utils.delete_apps_from_config_file()

@step(u'Then I dont see app anymore in configuration file')
def then_i_don_t_see_app_anymore_in_configuration_file(step):
    isAppList = False
    isList = False
    nbApp = 0

    for line in world.file.readlines():
        if utils.START_TOKEN in line:
            isAppList = True
            isList = True
        elif utils.END_TOKEN in line:
            isAppList = False
        elif isAppList:
            nbApp = nbApp + 1

    assert_equals(isList, True)
    assert_equals(nbApp, 0)


@step(u'When I add two lines at given index')
def when_i_add_two_lines_at_given_index(step):
    world.lines = ["new line 1", "new line 2"]
    utils.add_lines(TEST_FILE, world.lines, 2)
    world.file = open(TEST_FILE)

@step(u'And my lines appears at given index')
def and_my_lines_appears_at_given_index(step):
    file = open(TEST_FILE, "r")
    file_lines = file.readlines()
    assert_equals(file_lines[2], world.lines[0] + "\n")
    assert_equals(file_lines[3], world.lines[1] + "\n")

@step(u'And I have two applications marked as installed in my DB')
def and_i_have_two_applications_marked_as_installed_in_my_db(step):
    for app in App.objects.all():
        app.delete()

    app = App(name="Hello World 01", slug="hello-world-01")
    app.save()
    app = App(name="Hello World 02", slug="hello-world-02")
    app.save()
    
@step(u'When I set application list with installed application from DB')
def when_i_set_application_list_with_installed_application_from_db(step):
    utils.add_apps_to_config_file()


@step(u'Then Nginx configuration file has my two apps marked inside it')
def then_nginx_configuration_file_has_my_two_apps_marked_inside_it(step):    
    isAppList = False
    isList = False
    nbApp = 0

    for line in world.file.readlines():
        if utils.START_TOKEN in line:
            isAppList = True
            isList = True
        elif utils.END_TOKEN in line:
            isAppList = False
        elif isAppList and "hello-world-" in line:
            nbApp = nbApp + 1

    assert_equals(isList, True)
    assert_equals(nbApp, 2)

