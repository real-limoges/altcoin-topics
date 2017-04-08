'''
Sets up the tweepy class listener object for streaming
'''

import json
import tweepy
from auth_config import get_auth

class AltcoinListener(tweepy.StreamListener):
    '''
    Foo bar
    '''
    def __init__(self, coin):
        '''
        Initiates the stream with the given coin
        '''
        self.coin = unicode(coin.lower())

    def on_data(self, data):
        
        print json.loads(data)['text']
        return True

    def on_error(self, status_code):
        print status_code

        if status_code == 420:
            return False
        else:
            print "https://dev.twitter.com/overview/api/response-codes"
