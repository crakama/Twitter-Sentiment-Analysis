
import consumer_key

class ClassTwitter(object):

    def __init__(self):
        pass

    def search(self, query):

        twitter_ = consumer_key.authenticate()
        import ipdb;ipdb.set_trace()
        search_results = twitter_.search.tweets(
        q=query, count=count, lang='en', result_type='recent', screen_name=query)
