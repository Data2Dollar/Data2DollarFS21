# Importieren der benoetigten Bibliotheken 
import tweepy  
import pandas as pd

ACCESS_TOKEN = "1364569003474173952-Gfi9frQIyxAyLzKhg6NdJsHrRzlCSk"
ACCESS_SECRET = "h4NPfWBVveXkZk0bgijTFvpt7yx1aviUbSfhmhpQkyvPW"
CONSUMER_KEY = "ajPhLY0gkvXIWz96r2VzA3j3s"
CONSUMER_SECRET = "GRfDkopQvSQOCmw9AdJ5WYJ8R7VlNizXP4D4jYZ8CJjzCWNPOd"

def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

get_tweets = api.user_timeline('HSGStGallen')

tweet_list =[]
for tweet in get_tweets:
    tweet_id = tweet.id
    text = tweet.text

    tweet_list.append({'tweet_id':tweet_id, 
                'text':text})     

df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                       'text'])
df.to_csv('filename.csv', index=False, sep= ';')