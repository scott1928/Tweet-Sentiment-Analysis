from vaderSentiment.vaderSentiment import vaderSentiment
import tweepy	
import random
import time
import sys
import auth
import time
import datetime
used = open("scores.txt","r")

consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main_function():
	search = ["Brexit"]
	numberOfTweets = 200 
	analyzer = vaderSentiment.SentimentIntensityAnalyzer()
	compound = []
	for phrase in search:
		for tweet in tweepy.Cursor(api.search,q='brexit -filter:retweets',geocode='52.4862,-1.8904,300km',tweet_mode='extended').items(numberOfTweets):
			try:
					print('Tweet by: @'+tweet.user.screen_name)
					text = tweet.full_text
					print(text)
					vs = analyzer.polarity_scores(text)
					print(vs['compound'])
					compound.append(vs['compound'])
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				break
		print(len(compound))
		score = 0
		for item in compound:
			score = score + item
		if compound != []:
			average = score / len(compound)
		else:
			average = 0
		used = open("scores.txt","a")
		now = datetime.datetime.now()
		used.write(str(now.strftime("%Y-%m-%d %H:%M")))
		used.write(" ")
		used.write(str(average))
		used.write("\n")
	sys.stdout.close()

main_function()

                