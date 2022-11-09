import tweepy

# Replace the following strings with your own keys and secrets
TOKEN = 'Your TOKEN'
TOKEN_SECRET = 'Your TOKEN_SECRET'
CONSUMER_KEY = 'Your CONSUMER_KEY'
CONSUMER_SECRET = 'Your CONSUMER_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search_tweets(q="babson college", lang="en", count=10):
    print(f"{tweet.user.name}: {tweet.text}")