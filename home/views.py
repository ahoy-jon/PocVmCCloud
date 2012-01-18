from django.utils.simplejson import dumps
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.forms.models import model_to_dict

from gate.home.models import InstalledApp

def installed_apps(request):

    apps = []
    for app in InstalledApp.objects.all():
        apps.append(model_to_dict(app))

    content = dumps({ "rows": apps })
     
    return HttpResponse(content, mimetype="application/json")

