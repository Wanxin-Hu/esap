
bg= pd.read_csv(account + "_tweets_V1.csv")
fav_max = np.max(bg['favorite_count'])
rt_max  = np.max(bg['retweet_count'])

fav = bg[bg.favorite_count == fav_max].index[0]
rt  = bg[bg.retweet_count == rt_max].index[0]

# Max FAVs:
print("The tweet with more likes is: \n{}".format(bg['tweet'][fav]))
print("Number of likes: {}".format(fav_max))

# Max RTs:
print("The tweet with more retweets is: \n{}".format(bg['tweet'][rt]))
print("Number of retweets: {}".format(rt_max))



analysis = TextBlob(tweet)
if analysis.sentiment.polarity > 0:
    bg3['SA'] = 1
elif analysis.sentiment.polarity == 0:
    bg3['SA'] = 0
else:
    bg3['SA'] = -1


bg3['SA'] = np.array([sentiment(tweet) for tweet in bg3['tweet'] ])

pos_tweets = [ tweet for index, tweet in enumerate(bg3['tweet']) if bg3['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(bg3['tweet']) if bg3['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(bg3['tweet']) if bg3['SA'][index] < 0]

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(bg3['tweet'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(bg3['tweet'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(bg3['tweet'])))

sa =[pos_tweets,neu_tweets,neg_tweets]


    # Data to plot
labels = 'Positive', 'Negative', 'Neutral'
sizes = [len(pos_tweets)*100/len(bg3['tweet']), len(neu_tweets)*100/len(bg3['tweet']), len(neg_tweets)*100/len(bg3['tweet'])]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()