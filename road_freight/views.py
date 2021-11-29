from django.http import HttpResponse
from django.template.loader import render_to_string

def home_view(request, *args, **kwargs):
    HTML_STRING = render_to_string("home-view.html",{})
    #HTML_STRING = "<h1> hello </h1>"
    return HttpResponse(HTML_STRING)