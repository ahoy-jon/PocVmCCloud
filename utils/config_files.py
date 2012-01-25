from gate.settings import NGINX_CONF_FILE
from gate.home.models import InstalledApp as App


START_TOKEN = "### App List"
END_TOKEN = "### End App List"
APP_LINE_PREFIX = "     passenger_base_uri /apps/"

def delete_lines(filepath, startIndex, endIndex):
    '''
    In given file delete lines from startIndex to endIndex.
    '''

    file = open(filepath, "r")
    lines = file.readlines()
    file.close()

    del lines[startIndex:endIndex]

    file = open(filepath, "w")
    file.writelines(lines)
    file.close()


def add_lines(filepath, lines, index):
    '''
    Add given lines to file at given index.
    '''

    file = open(filepath, "r")
    filelines = file.readlines()
    file.close()

    i = index 
    for line in lines:
        if line:
            filelines.insert(i, "%s\n" % line)
        i = i + 1

    file = open(filepath, "w")
    file.writelines(filelines)
    file.close()


def delete_apps_from_config_file():
    '''
    Removes all app set inside Nginx configuration file.
    '''

    file = open(NGINX_CONF_FILE, "r")
    index = 0
    startIndex = 0
    endIndex = 0

    for line in file.readlines():        

        if START_TOKEN in line:
            startIndex = index
        elif END_TOKEN in line:
            endIndex = index 

        index = index + 1
    file.close()

    delete_lines(NGINX_CONF_FILE, startIndex + 1, endIndex)


def add_apps_to_config_file():
    '''
    Add installed app inside Nginx configuration file.
    '''

    file = open(NGINX_CONF_FILE, "r")
    index = 0
    startIndex = 0

    for line in file.readlines():
        index = index + 1
        if START_TOKEN in line:
            startIndex = index
    file.close()

    if startIndex > 0:
        linesToAdd = []
        for app in App.objects.all():
            if app.slug:
                linesToAdd.append("%s%s;" % (APP_LINE_PREFIX, app.slug))

        add_lines(NGINX_CONF_FILE, linesToAdd, startIndex)


def rebuild_config_file():
    '''
    Clear current application list set in Nginx config file and replace it with the 
    list of installed app.
    '''

    delete_apps_from_config_file()
    add_apps_to_config_file()

