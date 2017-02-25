from chiedza.settings import TONE_ANALYZER



def analyze(req):
    tweets = twitter.get_tweets(req)
    for tweet in tweets:
        tones = TONE_ANALYZER.tone(text=tweet, tones=emotion)
