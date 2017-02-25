
import tweepy


auth = tweepy.OAuthHandler('1BDeT59IM2QhW4C4w1LrkWvH3', 'v7xTClJOl5ckwnvzNzvs79BWZTlECeVK8EVjwFgFQlm8MAPX7N')
auth.set_access_token('836883541-2yjoPLmxZyQQqbNXBELFvxB5Ia4rT7VVe1xFLEDH', 'eQxanWaPPn8RVFfRUKbBb9IQvOiHLMX2NzTgjpgA1dF4h')

api = tweepy.API(auth)


def get_tweets(req):
    results = api.search(q=req, rpp=10, page=1)
    tweets = []
    for status in results:
        
