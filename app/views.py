
import json

from django.http import HttpResponse
from django.views.generic import TemplateView

from .analyzer import analyze
from .models import Result

# Create your views here.
class MainPage(TemplateView):
    template_name = 'app/index.html'


class ResultsPage(TemplateView):
    template_name = 'app/search.html'


def scrape_all(request):
    if request.GET:
        query = request.GET.get('search')
        results = analyze(query)
        Result.objects.create(
            query=query,
            positive=results.get('positive'),
            anger=results.get('anger'),
            sadness=results.get('sadness'),
            disgust=results.get('disgust'),
            percent_positive=results.get('percent_positive'),
            percent_negative=results.get('percent_negative')
        )
        return HttpResponse(json.dumps(results), content_type="application/json")
