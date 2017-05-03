#Posting a tweet programmatically using Python program

import tweepy

CONSUMER_KEY = "QluZ6AQ1FYlInBvrASVCfPp85" #"The key that you got tomorrow from your twitter account"
CONSUMER_SECRET = "cjrb8YUMWskE5ZneL8NNqpTs9JUvCy1S1GdV1DmWKvg8x1OybL"  # "The consumer secret"

ACCESS_KEY = "18245240-umk7Miiy5EXaXtpuC1lZ4MazS1fmnzpojc77DvNGG"   #"Access key that we created from our respective accounts in the end"
ACCESS_SECRET = "LVenbhZzjuH5o8zNC90Dg5Wp7C85tYnXs0jkEhJ7Gj3mU"   #"Access secret"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api=tweepy.API(auth)
api.update_status('Test tweet 2!')
for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass
