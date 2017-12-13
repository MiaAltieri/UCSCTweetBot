# TwitterBot
# Authors: Mia Altieri & Nick Leeds
# Date: 12/13/2017
# This program posts to twitter every 10 minutes from your desired Reddit thread.
# if no original Reddit post had been posted, wait for 10 minutes

# Tweets are posted to @UCSCTweetBot

from twython import Twython # Twitter-API_Wrapper
import praw # python-Reddit-API-Wrapper
import time

# global variables

# set Twitter credentials and create Twitter instance
app_key = 'UU5q3kRrcYDf0LVr6aeXNk9OX'
app_secret = 'NMt0hoFsTdzUJhDAU9nKPI0WAXmf4vcAaERixPeEKZe6u0UAE1'
oauth_token = '936316947947331584-1SVgp23nIBlMziITZp59q8Jea1pmflp'
oauth_token_secret = '5uYvL0LtKOYnVaFo8topsI1ISNDt7SIVASOv8VfW8YCEZ'
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

# set Reddit credentials and create Reddit instance
reddit = praw.Reddit(client_id='IdyNhUICtFuUPA',
                     client_secret='qS_R9mGDhDe8HJfEtsscim6FQKQ',
                     username='twitterbotUCSC',
                     password='UCSCslugs420',
                     user_agent='twitterUCSC')


# chooses which subreddit to pull data from
def post (reddit_thread):
    subreddit = reddit.subreddit(reddit_thread) # 'Showerthoughts')

    # infinite loop that attempts to tweet every 10 minutes
    while(True):
        new_tweet = subreddit.new() # pulls most recent post from reddit thread
        try: # attempts to post (if tweet is original)
            twitter.update_status(status=new_tweet.next().title)
            print("tweeted")
        except:
            print("no new tweet")
        time.sleep(600) # waits for ten minutes until attempting again

def main ():
    thread = input("What thread do you want to pull from, if none thread will default to 'Showerthoughts'\n")
    if (len(thread) == 0):
        thread = "Showerthoughts"
    post (thread)

if __name__ == '__main__':
    main()
