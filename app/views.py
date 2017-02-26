
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
        # results = {
        #     'positive': 0.15,
        #     'anger': 0.15,
        #     'sadness': 0.15,
        #     'disgust': 0.15,
        #     'percent_positive': 0.6,
        #     'percent_negative': 0.4,
        #     'top_tweets': [
        #         '<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Just checked in at Starbucks (Starbucks Coffee 神田駅前店) — <a href="https://t.co/629tnpyIq6">https://t.co/629tnpyIq6</a></p>— 👤 Ben Guild (@benguild) <a href="https://twitter.com/benguild/status/835741731509325825">February 26, 2017</a></blockquote>',
        #         '<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Just checked in at Starbucks (Starbucks Coffee 神田駅前店) — <a href="https://t.co/629tnpyIq6">https://t.co/629tnpyIq6</a></p>— 👤 Ben Guild (@benguild) <a href="https://twitter.com/benguild/status/835741731509325825">February 26, 2017</a></blockquote>',
        #         '<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Just checked in at Starbucks (Starbucks Coffee 神田駅前店) — <a href="https://t.co/629tnpyIq6">https://t.co/629tnpyIq6</a></p>— 👤 Ben Guild (@benguild) <a href="https://twitter.com/benguild/status/835741731509325825">February 26, 2017</a></blockquote>'
        #     ]
        # }
        return HttpResponse(json.dumps(results), content_type="application/json")
