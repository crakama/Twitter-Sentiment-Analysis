
import json
import oauth
import requests
import consumer_key
from alchemyapi import AlchemyAPI
from collections import Counter
from time import sleep
from tqdm import tqdm
from prettytable import PrettyTable


class ClassTwitter(object):

    def __init__(self):

        pass

    def wordFrequency(self, wordslist):
        """
        Performs word frequncy,reads data stored in the json file and display it
        """
        limit = 10
        dict_ = {}
        """ Perform word frequency """

        for word in wordslist:
            if word.isdigit():
                word = int(word)
            if word in dict_:
                dict_[word] = dict_[word] + 1
            else:
                dict_[word] = 1
        """ Write data to the JSON file """

        data_file = open('data.json', 'w')
        json.dump(dict_, data_file)

        """ Read data from JSON file """

        data_file = open('data.json', 'r')
        data = json.load(data_file)
        data_file.close()
        # # import ipdb
        # ipdb.set_trace()

        prettytable = PrettyTable(field_names=["Words", 'Word Frequency'])
        counter_ = list(Counter(data).items())

        """
           Count function has inbuild method-most_common,
           emitting it will pull AttributeError

        """
        table = [prettytable.add_row(row)
                 for row in counter_[:limit]]
        prettytable.add_column("Rankings", [i+1 for i in range(len(table))])
        prettytable.align["Words"], prettytable.align[
            'Word Frequency'] = 'l', 'r'
        print(prettytable)
        # import ipdb; ipdb.set_trace()

        newList = []
        for key in counter_:
            for row in key:
                newList.append(row)
        lis_ = str(newList)



        self.sentimentanalysis(lis_)

    def sentimentanalysis(self,text_):
        """
           Does sentiment analysis using SQLAlchemy API
        """
        alchemyapi = AlchemyAPI()
        response = alchemyapi.sentiment("text", text_)

        print "Sentiment: ", response["docSentiment"]["type"]


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
            # import ipdb;ipdb.set_trace()
            summary = "".join(status_texts).split(" ")


            print('#############################################################')

            if summary:
                # data_file = open('data.json', 'w')
                # json.dump(summary, data_file)
                # data_file.close()
                self.wordFrequency(summary)
        except Exception as e:
            print e
            print("No response! Check your internet connection")
