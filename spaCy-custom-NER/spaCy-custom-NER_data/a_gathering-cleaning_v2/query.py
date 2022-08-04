'''
Part of the Custom NER Label v2 architecture: DATA GATHERING

Objective: scraping tweets containing location information (street names) from Twitter

https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

Zekai Zhang, 29 July 2022
'''

import tweepy
import config 

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'NYC loop -is:retweet' 

'''search keywords:
1st attempt: "NYC" + "st", NOT retweet
    'search_test1_formatted.txt' (testing)
    'search_1_A_1005.txt' (batch A, 1005 tweets)

2nd attempt: "NYC" + "street"/"Street", NOT retweet
    'search_2_A_1000.txt' (batch A, 1000 tweets)

3rd attempt: "NYC" + "ave"/"avenue", NOT retweet
    'search_3_A_745.txt' (batch A, 745 tweets)

4th attempt: "NYC" + "Pl", NOT retweet
    'search_4_A_44.txt' (batch A, 44 tweets)

5th attempt: "NYC" + "Blvd", NOT retweet
    'search_5_A_66.txt' (batch A, 66 tweets)

6th attempt: "NYC" + "Ct", NOT retweet
    * NOT ideal result since returned results are mostly Connecticut

7th road/rd--not ideal

8th pkwy 17

9th lane--not ideal
10th ln--not ideal
11th drive--not ideal
12th terrace--not ideal
13th loop--not ideal
14th road/rd--not ideal

❗ Keep in mind of repeated tweets
'''

file_name1 = 'search.txt'


with open(file_name1, 'a+') as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=20).flatten(limit=1000):
        # print(tweet.text)
        filehandler.write( '%s\n\n' %tweet.text.replace('\n', ''))
