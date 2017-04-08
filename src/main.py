'''
This is the main module for collecting the stream of tweets
'''

import sys
import time
import tweepy

from altcoin_listener import AltcoinListener
from auth_config import get_auth
from requests.packages.urllib3.exceptions import ReadTimeoutError

if __name__ == '__main__':
    coin = sys.argv[1]

    twitter_authorization = get_auth()
    coin_stream = AltcoinListener(coin)
    coin_stream.start_db_conn()

    real_time_tweets = tweepy.Stream(
        auth=twitter_authorization,
        listener=coin_stream)
    try:
        real_time_tweets.filter(track=[coin])
    except ReadTimeoutError:
        time.time(10)
        real_time_tweets.filter(track=[coin])
