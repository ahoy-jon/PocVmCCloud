from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django import http


class RESTResource(object):
    """
    Dispatches based on HTTP method.
    """
    # Possible methods; subclasses could override this.
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    
    def __call__(self, request, *args, **kwargs):
        callback = getattr(self, request.method.upper(), None)
        if callback:
            return callback(request, *args, **kwargs)
        else:
            allowed_methods = [m for m in self.methods if hasattr(self, m)]
            return http.HttpResponseNotAllowed(allowed_methods)


# Simple views that return index page.
def home(request):
    return render_to_response('index.html')

