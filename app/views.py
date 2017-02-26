
import functools
import json
from datetime import timedelta

from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Sum

from .analyzer import analyze
from .models import Result

# Create your views here.
class MainPage(TemplateView):
    template_name = 'app/index.html'


class ResultsPage(TemplateView):
    template_name = 'app/search.html'


class TrendingPage(ListView):
    context_object_name = 'hot'
    template_name = 'app/trending.html'

    def _reduce(self, x, y):
        if not x.get(y.query):
            x[y.query] = 0
        x[y.query] += 1
        return x

    def get_queryset(self):
        queryset = Result.objects.filter(time__gte=timezone.now().date() - timedelta(days=7))
        result = functools.reduce(self._reduce, queryset, {})
        return result



def scrape_all(request):
    if request.GET:
        query = request.GET.get('search')
        results = analyze(query)

        Result.objects.create(
            query=query.lower().strip(),
            positive=results.get('positive'),
            anger=results.get('anger'),
            sadness=results.get('sadness'),
            disgust=results.get('disgust'),
            percent_positive=results.get('percent_positive'),
            percent_negative=results.get('percent_negative')
        )

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
        
        results['hist'] = [obj.as_dict() for obj in Result.objects.filter(query=query.lower().strip())]
        return HttpResponse(json.dumps(results), content_type="application/json")
