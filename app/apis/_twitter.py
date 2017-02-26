
from chiedza.settings import TWEEPY_API as api


def get_tweets(req):
    results = api.search(q=req, rpp=100)
    sorted(results, key=lambda x: x.favorite_count)
    tweets = []
    yield from results
