#Katy Madier | kmadier
#SI507 Waiver Part 1

# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
from twitter_keys_data import consumer_key, consumer_secret, access_token, access_token_secret
from nltk.corpus import *
from nltk import FreqDist

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# OUTPUT:
twitter_user_name=sys.argv[1]
twitter_name = api.get_user(twitter_user_name)
print("USER: " + twitter_name.screen_name)

# the number of tweets analyzed
tweet_number=int(sys.argv[2])
print("TWEETS ANALYZED: " + str(tweet_number))

#setting up the feed
all_tweets = api.user_timeline(screen_name=twitter_name.screen_name ,count=tweet_number)
list_of_words=[]
for tweet in all_tweets[:tweet_number]:
    words = nltk.word_tokenize(tweet.text)
    list_of_words+=words

for word in list(list_of_words):
    try:
        if word[0].isalpha() == False:
            list_of_words.remove(word);
        if "http" in word:
            list_of_words.remove(word);
        if "RT" in word:
            list_of_words.remove(word);
    except:
        print("An error has occurred!" + word)

#capitals before lowercase
sorted_list=sorted(list_of_words, key=lambda v: (v.upper(), v))

#tokenize
tagged = nltk.pos_tag(sorted_list)

# the five most frequent verbs that appear in the analyzed tweets
# a "verb" is anything that is tagged VB*
all_verbs=[]
for pair in tagged:
    if 'VB' in pair[1]:
        all_verbs+=[pair[0]]
fdistverb = FreqDist(w for w in all_verbs)

frequent_verbs=[]
for verb in fdistverb.most_common(5):
    frequent_verbs+=[str(verb[0])+ " (" + str(verb[1]) + ")"]
print("VERBS: " +", ".join(frequent_verbs))

# the five most frequent nouns that appear in the analyzed tweets
# a "noun" is anything that is tagged NN*
all_nouns=[]
for pair in tagged:
    if 'NN' in pair[1]:
        all_nouns+=[pair[0]]
fdistnoun = FreqDist(w for w in all_nouns)

frequent_nouns=[]
for noun in fdistnoun.most_common(5):
    frequent_nouns+=[str(noun[0]) + " ("+ str(noun[1]) + ")"]
print("NOUNS: " +", ".join(frequent_nouns))

# the five most frequent adjectives that appear in the analyzed tweets
# an "adjective" is anything that is tagged JJ*
all_adj=[]
for pair in tagged:
    if 'JJ' in pair[1]:
        all_adj+=[pair[0]]
fdistadj = FreqDist(w for w in all_adj)

frequent_adj=[]
for adj in fdistadj.most_common(5):
    frequent_adj+=[str(adj[0]) + " (" + str(adj[1]) +")"]
print("ADJECTIVES: " +", ".join(frequent_adj))

# the number of original tweets (i.e., not retweets)
original_tweets=[]
favorites=0
retweets=0
for tweet in all_tweets[:tweet_number]:
    if tweet.text.startswith("RT")==False:
        original_tweets+=[tweet.text]
        favorites+=tweet.favorite_count
        retweets+=tweet.retweet_count

print("ORIGINAL TWEETS: " + str(len(original_tweets)) )

# the number of times that the original tweets in the analyzed set were favorited
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(favorites) )

# the number of times that the original tweets in the analyzed set were retweeted by others
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(retweets) )

# Export CSV with 5 most common nouns
f = open("noun_data.csv","w")
f.write(str(tweet_number)+" tweets analyzed from "+twitter_name.screen_name+"'s Twitter feed.\nThese are the top 5 nouns and their frequencies.\n")
f.write("NOUN, NUMBER\n")
for noun in fdistnoun.most_common(5):
    f.write("{},{}\n".format(noun[0],noun[1]))
f.close()
