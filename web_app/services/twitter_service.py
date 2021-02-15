

# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv
from tweepy import OAuthHandler,API

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# def twitter_api():
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)


api=API(auth)
print("API CLIENT,"api)
user=api.get_user("s2t2")
print("TWITTER USER:",type(user))
breakpoint()



    