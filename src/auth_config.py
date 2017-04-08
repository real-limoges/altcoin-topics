from tweepy import OAuthHandler

def get_auth():
    with open('config/access_token') as f:
        access_token = f.read().strip()

    with open('config/access_secret') as f:
        access_secret = f.read().strip()

    with open('config/consumer_key') as f:
        consumer_key = f.read().strip()

    with open('config/consumer_secret') as f:
        consumer_secret = f.read().strip()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return auth
