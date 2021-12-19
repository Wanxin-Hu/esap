import tweepy
import twitter
import pandas as pd
import sys
import csv
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import re
from PIL import Image
import pandas_profiling 
import numpy as np 
import matplotlib as mpl
from os import path, getcwd
from textblob import TextBlob


def get_tweets(username): 
    
	auth = tweepy.OAuthHandler('tp7eQE6b3fgPZwWfQVA0DLPdU', 'AjXzemxrdRGuams2DRhuR3QS5iIx5w2mkrNo2ETaGwdmpc5yCy')
	auth.set_access_token('3000298052-OaC61ZxzH6eTl2XOfYWs8LMNfv5Pq1gF97o8gVf', 'YBS465hDtQuqFLkMFCjKFyoWoFNg6AWiasAlzyWboAz0l') 
	api = tweepy.API(auth) 
	tfile = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items():

    #username, tweet id, date/time, text
		tfile.append([username, tweet.id_str,tweet.source, tweet.created_at,tweet.retweet_count,tweet.favorite_count, tweet.text])

#write to a new csv file from the array of tweets
	outfile = username + "_tweets_V1.csv"
	#print ("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerow(['user_name', 'tweet_ID', 'source', 'created_date','retweet_count','favorite_count','tweet'])
		writer.writerows(tfile)

def generate_wordcloud_image(words, mask):
	#word_cloud = WordCloud(width = 512, height = 512, background_color='white',max_words=5000	,stopwords=STOPWORDS, mask=mask,contour_width=0.5, contour_color='navy' , prefer_horizontal=0.5, relative_scaling=0.5).generate(words)
	word_cloud = WordCloud(background_color = 'white', max_words = 6000, mask = mask, max_font_size = 90, random_state = 60).generate(words)
	image_colors = ImageColorGenerator(mask)
	plt.figure(figsize=(20,10),facecolor = 'white', edgecolor='red')
	plt.imshow(word_cloud.recolor(color_func = image_colors),interpolation='bilinear')
	plt.axis('off')
	plt.tight_layout(pad=0)
	plt.show()
	#fig.saveifg('word.png', dpi = 1400)

def generate_wordcloud_square(text):
	wordcloud = WordCloud(background_color='white',stopwords=STOPWORDS,max_words=300,max_font_size=60, random_state=60).generate(str(text))
	fig = plt.figure(1)
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()
	fig.savefig("word1.png", dpi=1400)

def sentiment(tweet):
	analysis = TextBlob(tweet)
	if analysis.sentiment.polarity >0:
		return 1
	elif analysis.sentiment.polarity ==0:
		return 0
	else:
		return -1

def chart(account):
	twee = pd.read_csv(account + '_tweets_V1.csv')
	fav_max = np.max(twee['favorite_count'])
	rt_max = np.max(twee['retweet_count'])

	fav = twee[twee.favorite_count == fav_max].index[0]
	rt = twee[twee.retweet_count == rt_max].index[0]

	print('The tweet with more likes is: \n{}'.format(twee['tweet'][fav]))
	print('Number of like: {}'.format(fav_max))

	print('The tweet with more retweets is: \n{}'.format(twee['tweet'][rt]))
	print('Number of retweets: {}'.format(rt_max))

	twee['SA'] = np.array([sentiment(tweet) for tweet in twee['tweet']])

	pos_tweets = [tweet for index, tweet in enumerate(twee['tweet']) if twee['SA'][index]>0]
	neu_tweets = [tweet for index, tweet in enumerate(twee['tweet']) if twee['SA'][index]==0]
	neg_tweets = [tweet for index, tweet in enumerate(twee['tweet']) if twee['SA'][index]<0]

	print("Percentage of positive tweets: {}%".format(round(len(pos_tweets)*100/len(twee['tweet'])), 2))
	print("Percentage of neutral tweets: {}%".format(round(len(neu_tweets)*100/len(twee['tweet'])),2))
	print("Percentage de negative tweets: {}%".format(round(len(neg_tweets)*100/len(twee['tweet'])),2))

	sa = [pos_tweets, neu_tweets, neg_tweets]

	#izes = [len(pos_tweets)*100/len(twee3['tweet']), len(neu_tweets)*100/len(bg3['tweet']), len(neg_tweets)*100/len(bg3['tweet'])]
	explode = (0.1, 0, 0)
	plt.pie([len(pos_tweets)*100/len(twee['tweet']), len(neu_tweets)*100/len(twee['tweet']), len(neg_tweets)*100/len(twee['tweet'])], labels = ['Positive' , 'Negative', 'Neutral'], colors = ['gold','coral','skyblue'], shadow = True, startangle = 140, explode = explode, autopct='%1.1f%%')
	plt.axis('equal')
	plt.show()

def main():
	print('This program will print a WORDCLOUD of the most frequent words of your twitter and also the sentiment of the words!')
	account = input("Type a twitter account: ")
	# user name
	get_tweets(account)

	twee = pd.read_csv(account + "_tweets_V1.csv") 
	#print(bg)

	x = twee[9:10]['tweet']

	twee2 = []
	pattern1 = re.compile(" ' # S % & ' ( ) * + , - . / : ; < = >  @ [ / ] ^ _ { | } ~")
	pattern2 = re.compile("@[A-Za-z0-9]+") 
	pattern3 = re.compile("https?://[A-Za-z0-9./]+")

	for item in twee["tweet"]:
	    tweet = re.sub(pattern1, "", item)
	    tweet = re.sub(pattern2, "", tweet)
	    tweet = re.sub(pattern3, "", tweet)
	    twee2.append(tweet)

	twee3 = pd.DataFrame(twee2, columns = ["tweet"])

	#print(bg2)

	mpl.rcParams['figure.figsize']=(16.0,10.0)    
	mpl.rcParams['font.size']=12     
	mpl.rcParams['savefig.dpi']=1400
	mpl.rcParams['figure.subplot.bottom']=.1

	stopwords = set(STOPWORDS)
	text = " ".join(tweet for tweet in twee3.tweet)
	#print ("There are {} words in the combination of all tweets.".format(len(text)))
	num = int(input('enter number for the shape you want!!\nHeart : 1, Circle : 2, Star : 3, arrow : 4, square : 5\n'))

	if num == 1:
		mask = np.array(Image.open(path.join('heart2.png')))
	elif num == 2:
		mask = np.array(Image.open(path.join('circle.png')))
	elif num ==3:
		mask = np.array(Image.open(path.join('star.png')))
	elif num == 4:
		mask = np.array(Image.open(path.join('arrow4.png')))
	elif num == 5:
		mask = np.array(Image.open(path.join('square2.png')))

	word = ' '.join(review for review in twee3.tweet)
	for i in range(0, len(word)-1):
		if word[i:i+2] == 'RT':
			word = word[:i] + word[i+2:]

	generate_wordcloud_image(word, mask)

	#generate_wordcloud_square(word)
	chart(account)

main()