import random
import tweepy
from dotenv import load_dotenv
import os
from nltk.tokenize import sent_tokenize

# Load env variables
load_dotenv()

# APP Credentials to access the Twitter API
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Bot account credentials after we are done with the PIN-based 3 legged OAuth authentication
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Tweepy’s interface for making requests to Twitter API v2 endpoints is Client.
client = tweepy.Client(
    BEARER_TOKEN,
    API_KEY,
    API_KEY_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

with open('corpus_leviathan.txt', 'r', encoding='utf-8-sig') as book:
	entireBook = book.read()					# Read the whole book as a string
	#print(entireBook[3768])					# Prints the initial T
	#print(entireBook[1213027]) 				# Prints the final S
	finalBook = entireBook[3768:1213028]		# We only want the actual book
	sentences = sent_tokenize(finalBook)		# Split the book into sentences using NLP
	randomSentence = random.choice(sentences)	# Pick a random sentence from the list

	# Tweet's can't exceede 280 characters
	# Don't include short strings because those are not actual sentences
	while(len(randomSentence) >= 280 or len(randomSentence) < 8):
		randomSentence = random.choice(sentences)
	
	#print(randomSentence)
	client.create_tweet(text=randomSentence)	# Send the Tweet

