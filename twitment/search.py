
import json
import oauth
import requests
import consumer_key


class ClassTwitter(object):

    def __init__(self):
        pass

    def search(self, query):

        try:
            twitter_ = consumer_key.authenticate()
            # import ipdb;ipdb.set_trace()
            ''' search_results gets authentication from <twitter_> and
                searches for the tweets made by <screen_name>
            '''
            search_results = twitter_.search.tweets(
                q=query, lang='en', result_type='recent', screen_name=query)
            # import ipdb;ipdb.set_trace()
            print search_results
            '''
              statuses is a list of dict that contains all data about the user
            '''
            statuses = search_results['statuses']

            ''' status['text'] only accesses the value inside the <text> key,
                which is the user's tweet
            '''

            status_texts = [status['text'].strip() for status in statuses]
            status_texts = [status.replace("\"", "")
                            for status in status_texts]
            summary = "".join(status_texts).split(" ")

            if summary:
                data_file = open('data.json', 'w')
                json.dump(summary, data_file)
                data_file.close()
        except:
            print("No response! Check your internet connection")

    def wordFrequency():
        pass
