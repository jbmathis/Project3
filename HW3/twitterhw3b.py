# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from virus import consumer_key, consumer_secret, access_token, access_token_secret
from textblob import TextBlob

#Boilerplate Code
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
#search for tweets about dogs
api = tweepy.API(auth)
tweets = api.search('Dogs')
total = 0
polarity = 0
subjectivity = 0
#print out all of the tweets and add up the polarities and subjectivities
for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	ps_tuple = analysis.sentiment
	polarity += ps_tuple[0]
	subjectivity += ps_tuple[1]
	total += 1
#take the total subjectivity and polarity and divide by the total number of tweets
avg_subjectivity = subjectivity / total
avg_polarity = polarity / total
print("Average subjectivity is", avg_subjectivity)
print("Average polarity is", avg_polarity)

