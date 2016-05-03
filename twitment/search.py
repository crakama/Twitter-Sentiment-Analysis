
import json
import oauth
import requests
import consumer_key
from time import sleep
from tqdm import tqdm


class ClassTwitter(object):

    def __init__(self):

        pass

    def wordFrequency(self, wordslist):
        # wordslist = wordlst.split()

        dict_ = {}

        for word in wordslist:
            if word.isdigit():
                word = int(word)
            if word in dict_:
                dict_[word] = dict_[word] + 1
            else:
                dict_[word] = 1
        return dict_

        for key, value in dict_:
            return key, value

    def search(self, query):

        try:
            twitter_ = consumer_key.authenticate()
            # import ipdb;ipdb.set_trace()
            ''' search_results gets authentication from <twitter_> and
                searches for the tweets made by <screen_name>
            '''
            range_ = 10
            for key in tqdm(range(range_)):
                sleep(0.01)
                search_results = twitter_.search.tweets(
                q=query, lang='en', result_type='recent', screen_name=query)
                # print search_results
            # import ipdb;ipdb.set_trace()


            '''
              statuses is a list of dict that contains all data about the user
            '''
            statuses = search_results['statuses']

            ''' status['text'] only accesses the value inside the <text> key,
                which is the user's tweet
            '''

            status_texts = [status['text'].strip() for status in statuses]
            status_texts = [status.replace('"', '')
                            for status in status_texts]
            summary = "".join(status_texts).split(" ")

            print('#################################')
            print self.wordFrequency(summary)


            if summary:
                data_file = open('data.json', 'w')
                json.dump(summary, data_file)
                data_file.close()
        except:
            print("No response! Check your internet connection")

