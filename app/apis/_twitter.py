
from chiedza.settings import TWEEPY_API as api


def get_tweets(req):
    results = api.search(q=req, lang='en', rpp=100)
    results = sorted(results, key=lambda x: x.favorite_count, reverse=True)
    tweets = []
    yield from results
