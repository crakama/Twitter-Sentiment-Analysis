import twitter

def authenticate():
    CONSUMER_KEY = 'BAKDTiFR9tvGl9HwUqHn3VfwW'
    CONSUMER_SECRET = 'VD0CBzlxxMCV3ya746drzG9Z9VLWp55YuOxmCMunmIN8E154iv'
    OAUTH_TOKEN = '324805546-8vOSeTDQQLsSZhPh1pNI1eELsU0MCU7E3fUBdbbh'
    OAUTH_TOKEN_SECRET = 'wZ8vNzKe5K7n3YyZ7LKITFtmveRtHQ2s2CTYHNMGdjNBc'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return twitter_api


