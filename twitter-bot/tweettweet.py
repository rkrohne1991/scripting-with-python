import tweepy
import time

# Consumer Keys & Authentication Tokens for TwitterBot Project
consumer_key = "makyXADeWqm5J19uX7umY1T7o"
consumer_secret = "PAlNlbQL6nxdWz20yOBTOQSHHbahPdXD6gRaD6tJfTCnpudd8m"
access_token = "1305847114283573250-kJEYumaAdDTokK2vQ5pjie9GxCWJWf"
access_token_secret = "TFdUzgpXrchqRAxhsjUZzcmhcCWYSY4NHlNuGERPrdX7u"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = "Andrei Neagoie"
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print("I like that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     # name of person to find in your followers
#     follower_name_to_follow = "Joanna Wojcik"
#     if follower.name == follower_name_to_follow:
#         follower.follow()
#         break
