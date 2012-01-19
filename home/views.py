from django.utils.simplejson import dumps, loads
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from gate.core.views import RESTResource
from gate.home.models import InstalledApp


class InstalledAppsResource(RESTResource):
    '''
    Resources to list and create installed application
    '''


    def format(self, app, full=False):
        '''
        Convert app object to dict.
        '''

        return model_to_dict(app)
        

    def parse(self, json):
        """
        Convert from a JSON object to an App object.
        """

        d = loads(json)
        try:
            return InstalledApp(
                name = force_unicode(d['name']),
                slug = force_unicode(d['slug']),
            )
        except (ValueError, KeyError, TypeError):
            return None


    def GET(self, request):
        '''
        Returns list of installed applications.
        '''

        apps = []
        for app in InstalledApp.objects.all():
            apps.append(self.format(app))

        content = dumps({ "rows": apps })         
        return HttpResponse(content, mimetype="application/json")


    def POST(self, request):
        '''
        Create a new application from posted informations.
        '''
        app = self.parse(request.raw_post_data)
        if not app:
            return HttpResponseBadRequest()
        
        dbApp = InstalledApp.objects.filter(slug=app.slug)
        if not dbApp:
          app.save()

        return HttpResponse(status=201) # HTTP 201 Created


class InstalledAppResource(RESTResource):
    '''
    Resources to work on a given application identified by its slug.
    '''

    def DELETE(self, request, slug):
        '''
        Remove and uninstall application identified by slug.
        '''

        app = get_object_or_404(InstalledApp, slug=slug)
        app.delete()
        return HttpResponse(status=200)

