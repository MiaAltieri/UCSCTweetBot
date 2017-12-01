from twython import Twython
import praw
import time

# Twitter credentials
app_key = 'UU5q3kRrcYDf0LVr6aeXNk9OX'
app_secret = 'NMt0hoFsTdzUJhDAU9nKPI0WAXmf4vcAaERixPeEKZe6u0UAE1'
oauth_token = '936316947947331584-1SVgp23nIBlMziITZp59q8Jea1pmflp'
oauth_token_secret = '5uYvL0LtKOYnVaFo8topsI1ISNDt7SIVASOv8VfW8YCEZ'
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

# Reddit credentials
reddit = praw.Reddit(client_id='IdyNhUICtFuUPA',
                     client_secret='qS_R9mGDhDe8HJfEtsscim6FQKQ',
                     username='twitterbotUCSC',
                     password='UCSCslugs420',
                     user_agent='twitterUCSC')

# chooses which subreddit to pull data from
subreddit = reddit.subreddit('Showerthoughts')

# infinite loop that attempts to tweet every 10 minutes
while(True):
    new_tweet = subreddit.new()
    try:
        twitter.update_status(status=new_tweet.next().title)
        print("tweeted")
    except:
        print("no new tweet")
    time.sleep(600)
    
