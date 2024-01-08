### Twitter Bot

This bot tweets random fragments from the 1651 edition of Hobbes' Leviathan
Built using Python and Tweepy

https://twitter.com/LeviathanOOC

For more information, see https://docs.tweepy.org/en/stable/

### Quickstart

First, create the virtual env and install the packages
```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

We will be using the Punkt Sentence Tokenizer
For more information, see https://www.nltk.org/api/nltk.tokenize.punkt.html
To install the model, you can run
```python
python get_nltk_data.py
```

Now you need to get the credentials to authenticate to the Twitter API v2
You will need the following:
1. Consumer key (API Key)
2. Consumer secret (API Key Secret)
3. Bearer Token
4. Access Token
5. Access Token Secret

We are assuming that you have two Twitter accounts
One is your main account where you have a developer account
The other is your bot account

1, 2 and 3 are obtained from your developer account
4, 5 are generated by performing the PIN-based 3 legged OAuth
You can do this by running
```python
python oauth.py
```

Once you have all the credentials you can create an .env file under src/
Following the env_sample file paste your credentials in the .env file
For more information, see https://pypi.org/project/python-dotenv/

Now you should be able to make a post by running
```python
python levbot.py
```
