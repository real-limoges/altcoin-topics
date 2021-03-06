'''
Sets up the tweepy class listener object for streaming
'''

import json
import tweepy
import pymongo


class AltcoinListener(tweepy.StreamListener):
    '''
    Listener object for given coin's ticker.
    '''

    def __init__(self, coin):
        '''
        Initiates the stream with the given coin
        '''
        self.coin = unicode(coin.lower())
        self.coll = None

    def start_db_conn(self):
        '''
        @params: None
        @returns: Sets up MongoDB connection and collections
        '''
        client = pymongo.MongoClient()
        mongodb = client['altcoin-data']
        self.coll = mongodb[self.coin]

    def on_data(self, data):
        '''
        @params: Data (streamed from Tweepy Stream)
        @returns: None

        Ingests the filtered data and extracts the text.
        '''
        text = json.loads(data)['text']
        if text.startswith('rt'):
            pass
        elif self.coin in [word.lower() for word in text.split(' ')]:
            print json.loads(data)['text']
            self.coll.insert_one(json.loads(data))

    def on_error(self, status_code):
        '''
        @params: status_code (int)
        @returns: False if code is 420. Else prints response codes link
                  to screen
        '''
        if status_code == 420:
            return False
        else:
            print status_code
            print "https://dev.twitter.com/overview/api/response-codes"
