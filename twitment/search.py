import os
import json
import oauth
import requests
import consumer_key
from stop_words import StopWords
from alchemyapi import AlchemyAPI
from collections import Counter
from time import sleep
from tqdm import tqdm

from prettytable import PrettyTable

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from colorama import init
from colorama import Fore, Back, Style
init()


file_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(file_path)


class ClassTwitter(object):

    def __init__(self):

        pass

    def colorify(text, colors):
        """Prefix and suffix text to render terminal color"""



    def stop_words(self, dirtywords):
        """ Remove the stop words  """
        cleanwords = []
        dirt = []
        with open('stop_words.json','r') as f:
            data = json.loads(f.read())
            stopwords = data['stopwords']
            print stopwords

        return [word for word in dirtywords if word not in stopwords]

    def wordFrequency(self, wordslist):
        """
            Performs word frequncy,reads data stored in the json file
            and display it
        """
        self.wordslist = self.stop_words(wordslist)
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

        # import ipdb; ipdb.set_trace()
        print Fore.GREEN + "  "
        prettytable = PrettyTable(field_names=["Words", 'Word Frequency'],header_color='yellow,bold')
        counter_ = Counter(data)

        """
           Count function has inbuild method-most_common,
           emitting it will pull AttributeError

        """
        table = [prettytable.add_row(row)
                 for row in counter_.most_common()[:limit]]

        prettytable.add_column("Rankings", [i+1 for i in range(len(table))])
        prettytable.align["Words"], prettytable.align[
            'Word Frequency'] = 'l', 'r'
        print(prettytable)

        print(Style.RESET_ALL)

        self.sentimentanalysis(dict_)

    def sentimentanalysis(self, text_):
        """
           Does sentiment analysis using SQLAlchemy API
        """
        alchemyapi = AlchemyAPI()
        # import ipdb; ipdb.set_trace()
        if "" in text_.keys() and len(text_) < 2:

            print "No tweets to analyse were found!!"
        else:
            response = alchemyapi.sentiment("text", text_)
            sentrep = response["docSentiment"]["type"]
            lst = [sentrep]

        prettytable = PrettyTable(['Sentiment Type'])

        t = prettytable.add_row(lst) 

        print prettytable
  


    def search(self, query):

        try:
            twitter_ = consumer_key.authenticate()

            ''' search_results gets authentication from <twitter_> and
                searches for the tweets made by <screen_name>
            '''
            range_ = 10
            for key in tqdm(range(range_)):
                sleep(0.01)
                search_results = twitter_.search.tweets(
                    q=query, lang='en', result_type='recent', screen_name=query)

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
            fetchedtweets = "".join(status_texts).split(" ")

            if fetchedtweets:

                self.wordFrequency(fetchedtweets)
            else:
                return "No tweet has been fetched"
        except Exception as e:
            print e
            print("No response! Check your internet connection")

    def sendTweet(self, num):

        username = "CATHERINERAKAMA"
        apikey = "676dbd926bbb04fa69ce90ee81d3f5ffee2692aaf80eb5793bd70fe93e77dc2e"

        to = num

        """ Read data from JSON file """
        data_file = open('data.json', 'r')
        data = json.load(data_file)
        data_file.close()

        message = data
        # Create a new instance of our awesome gateway class
        gateway = AfricasTalkingGateway(username, apikey)
        # Any gateway errors will be captured by our custom Exception class below,
        # so wrap the call in a try-catch block
        try:
            # Thats it, hit send and we'll take care of the rest.
            results = gateway.sendMessage(to, message)

            for recipient in results:
                # status is either "Success" or "error message"
                print 'Message sent to number=%s;status=%s' % (recipient['number'],
                                                               recipient[
                    'status'])
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while sending: %s' % str(e)
