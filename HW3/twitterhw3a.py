# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
from virus import consumer_key, consumer_secret, access_token, access_token_secret

#Boilerplate Code
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#use api to publish a tweet with the specified photo and text
api = tweepy.API(auth)
tweet_text = '#UMSI-206 #Proj3'
tweet = api.update_with_media('cat_code.png', tweet_text)