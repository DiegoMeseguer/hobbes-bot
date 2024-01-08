import tweepy
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, callback='oob')
redirectURL = auth.get_authorization_url()

print(redirectURL)

# Now the user bot is supposed to go their browser and paste the redirectURL and then get the PIN

verifier = input("Input PIN: ")

accessToken, accessTokenSecret = auth.get_access_token(verifier)

# Paste these in your script
print("Your credentials are:")
print(accessToken)
print(accessTokenSecret)

