
import json

from django.http import HttpResponse
from django.views.generic import TemplateView
from .analyzer import analyze
# Create your views here.
class MainPage(TemplateView):
    template_name = 'app/index.html'


class ResultsPage(TemplateView):
    template_name = 'app/search.html'


def scrape_all(request):
    if request.GET:
        query = request.GET.get('search')
        results = analyze(query)
        return HttpResponse(json.dumps(results), content_type="application/json")
