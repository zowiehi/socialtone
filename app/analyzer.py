from chiedza.settings import TONE_ANALYZER



def analyze(req):


    tweets = twitter.get_tweets(req)
    twitter_average = 0
    tweet_count = 0
    for tweet in tweets:
        tweet_count += 1
        tones = TONE_ANALYZER.tone(text=tweet, tones=emotion)
        positive_tone = filter(lambda x: x.tone_name == 'joy', tones.document_tone.tone_categories[0].tones)
        positive_percent = positiveTone[0].score

        # angerTone = filter(lambda x: x.tone_name == 'anger', tones.document_tone.tone_categories[0].tones)
        # negativePercent = angerTone[0].score
        #
        # sadnessTone = filter(lambda x: x.tone_name == 'sadness', tones.document_tone.tone_categories[0].tones)
        # negativePercent += sadnessTone[0].score
        #
        # disgustTone = filter(lambda x: x.tone_name == 'disgust', tones.document_tone.tone_categories[0].tones)
        # negativePercent += disgustTone[0].score

        score = positivePercent * 5
        twitter_average += score

    twitter_average /= tweet_count

    
