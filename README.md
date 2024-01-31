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
To install the model, run
```python
python get_nltk_data.py
```

Now we need to get the credentials to authenticate to the Twitter API v2  
We will need the following:
1. Consumer key (API Key)
2. Consumer secret (API Key Secret)
3. Bearer Token
4. Access Token
5. Access Token Secret

We are assuming that there are two Twitter accounts:  
The first one is the main account where one has an approved developer account  
The second one is the bot account  

Credentials 1, 2 and 3 are obtained from the developer account  
Create an .env file under src/ (see the env_sample file)  
Passte your credentials in the .env file  

Now we can generate credentials 4 and 5 by performing the PIN-based 3 legged OAuth  
We can do this by running  
```python
python oauth.py
```

Once we have the last credentials we can paste them in the .env file  
For more information, see https://pypi.org/project/python-dotenv/

Now we should be able to make a post by running
```python
python levbot.py
```
