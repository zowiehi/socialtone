from chiedza.settings import TONE_ANALYZER



def analyze(req):


    tweets = twitter.get_tweets(req)

    twitter_average = 0
    positive_average = 0
    anger_average = 0
    sadness_average = 0
    disgust_average = 0

    tweet_count = 0
    top_tweets = []
    for tweet in tweets:
        tweet_count += 1
        if(tweet_count <= 3):
            top_tweets.append(tweet)
        tones = TONE_ANALYZER.tone(text=tweet.text, tones=emotion)
        positive_tone = filter(lambda x: x.tone_name == 'joy', tones.document_tone.tone_categories[0].tones)
        positive_percent = positiveTone[0].score
        positive_average += positive_percent

        angerTone = filter(lambda x: x.tone_name == 'anger', tones.document_tone.tone_categories[0].tones)
        negativePercent = angerTone[0].score
        anger_average += angerTone[0].score

        sadnessTone = filter(lambda x: x.tone_name == 'sadness', tones.document_tone.tone_categories[0].tones)
        negativePercent += sadnessTone[0].score
        sadness_average += sadnessTone[0].score

        disgustTone = filter(lambda x: x.tone_name == 'disgust', tones.document_tone.tone_categories[0].tones)
        negativePercent += disgustTone[0].score
        disgust_average += disgustTone[0].score

        score = positivePercent * 5
        twitter_average += score

    twitter_average /= tweet_count
    positive_average /= tweet_count
    anger_average /= tweet_count
    sadness_average /= tweet_count
    disgust_average /= tweet_count

    results = {
    'twitter_average' : twitter_average,
    'positive' : positive_average,
    'anger' : anger_average,
    'sadness' : sadness_average,
    'disgust' : disgust_average,
    'top_tweets' : top_tweets
    }
