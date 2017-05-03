#Posting a tweet programmatically using Python program

import tweepy

CONSUMER_KEY = "xxxx" #"The key that you got tomorrow from your twitter account"
CONSUMER_SECRET = "xxxx"  # "The consumer secret"

ACCESS_KEY = "xxxx"   #"Access key that we created from our respective accounts in the end"
ACCESS_SECRET = "xxxx"   #"Access secret"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api=tweepy.API(auth)
api.update_status('Test tweet 2!')
for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass
