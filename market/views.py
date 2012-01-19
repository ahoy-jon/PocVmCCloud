from django.utils.simplejson import dumps
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.forms.models import model_to_dict

from gate.core.views import RESTResource
from gate.market.models import App


class AppsResource(RESTResource):
    '''
    Retrieve list of available applications in the market place.
    '''

    def GET(self, request):
        apps = []
        for app in App.objects.all():
            apps.append(model_to_dict(app))

        content = dumps({ "rows": apps })         
        return HttpResponse(content, mimetype="application/json")


