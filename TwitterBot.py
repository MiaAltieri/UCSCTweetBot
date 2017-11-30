from twython import Twython
import praw

APP_KEY = 'UU5q3kRrcYDf0LVr6aeXNk9OX'
APP_SECRET = 'NMt0hoFsTdzUJhDAU9nKPI0WAXmf4vcAaERixPeEKZe6u0UAE1'
OAUTH_TOKEN = '936316947947331584-1SVgp23nIBlMziITZp59q8Jea1pmflp'
OAUTH_TOKEN_SECRET = '5uYvL0LtKOYnVaFo8topsI1ISNDt7SIVASOv8VfW8YCEZ'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

reddit = praw.Reddit(client_id = 'E8cMmZx6DvPs2A',
                     client_secret = 'xP1GI9UZP-337Kmmw5dfcvi5qd8',
                     username = 'RedditSlug',
                     password = 'cookies',
                     user_agent = 'test by /u/RedditSlug')

def tweet(entry):
    twitter.update_status(status=entry)

def getTweet():
    subreddit = reddit.subreddit('Showerthoughts')
    new_thoughts = subreddit.new(limit=100)
    for submission in new_thoughts:
        return submission.title

text = getTweet()
tweet(text)

