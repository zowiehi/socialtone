
from chiedza.settings import TWEEPY_API as api


def get_tweets(req):
    results = api.search(q=req, rpp=100, page=1)
    tweets = []
    count = 0
    for status in results:
        if(count > 20):
            break
        if(status.favorite_count > 10):
            tweets.append(status.text)

    return tweets
