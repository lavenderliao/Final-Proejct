import tweepy

# Replace the following strings with your own keys and secrets
TOKEN = '4843502113-MG1cV4TPuDfQ4caXt6RcxRCqAESxcXgMb3Jdk5i'
TOKEN_SECRET = 'eM1cdllhkaog23rblMwvN8VM22GoDZjVZ3MAgDMSNZbHy'
CONSUMER_KEY = 'Am8VYSofqviOVCav30MZEc6tf'
CONSUMER_SECRET = 'LYnt2JgALhtpiDueDLyOCj1Ys1CtkTrEc64EXNDPZrSm85fGVL'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search_tweets(q="babson college", lang="en", count=10):
    print(f"{tweet.user.name}: {tweet.text}")