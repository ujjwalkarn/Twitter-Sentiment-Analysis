### Disclaimer: This tutorial and the code in this repository are pretty old and are not supported anymore. I would recommend using newer tutorials available on the web in case you want to try sentiment analysis on Twitter data.

This repository contains a tutorial for carrying out sentiment analysis on Twitter livestream data. 

As a part of this tutorial, we can do the following:

- Access Twitter live stream and captured tweets using the oauth2 library and Twitter REST API.
- Parse raw tweets obtained in JavaScript Object Notation.
- Compute term frequency histogram of the livestream data for calculating tweet sentiments.
- Query the raw tweet data for various parameters of interest like hashtags, origin of the tweet.
- Find top ten hashtags across the tweet data.

1. Getting Twitter Data
-------------------
To access the live stream, you will need to install the oauth2 library so you can properly authenticate.
```
$ pip install oauth2
```
The steps below will help you set up your twitter account to be able to access the live stream.

1. Create a twitter account if you do not already have one.
2. Go to [Twitter Dev](https://dev.twitter.com/apps) and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5. On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
6. Click the button "Create My Access Token". You can Read more about Oauth authorization.
7. You will now copy four values into `twitterstream.py`. These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". All four should now be visible on the API Keys page. (You may see "API Key" referred to as "Consumer key" in some places in the code or on the web; they are synonyms.) 
8. Open `twitterstream.py` and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:
  - api_key = "Enter api key"
  - api_secret = "Enter api secret"
  - access_token_key = "Enter your access token key here"
  - access_token_secret = "Enter your access token secret here"
9. Run the following and make sure you see data flowing and that no errors occur `$ python twitterstream.py > output.txt`
10. This command pipes the output to a file. Stop the program with Ctrl-C, but wait at least 3 minutes for data to accumulate.
11. If you wish, modify the file to use the twitter search API to search for specific terms. For example, to search for the term "microsoft", you can pass the following url to the twitterreq function: `https://api.twitter.com/1.1/search/tweets.json?q=microsoft`

2. Deriving the sentiment of each tweet
------------------------------------------
For this part, we will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. See the file AFINN-README.txt for more information

You can read the [Twitter documentation](https://dev.twitter.com/overview/api/tweets) to understand what information each tweet contains and how to access it, but it's not too difficult to deduce the structure by direct inspection.

The file `tweet_sentiment.py` contains the code used for deriving the sentiment of each tweet.

3. Deriving the sentiment of new terms
------------------------------------------
Here's how you might think about the problem: We know we can use the sentiment-carrying words in AFINN-111.txt to deduce the overall sentiment of a tweet. Once you deduce the sentiment of a tweet, you can work backwards to deduce the sentiment of the non-sentiment carrying words that do not appear in AFINN-111.txt. For example, if the word soccer always appears in proximity with positive words like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.

The following [paper](http://www.cs.cmu.edu/~nasmith/papers/oconnor+balasubramanyan+routledge+smith.icwsm10.pdf) may be helpful for developing a sentiment metric. 

The file `term_sentiment.py` contains the code used for deriving the sentiment of new terms.

4. Computing Term Frequency
------------------------------------------
The frequency of a term can be calculated as `[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]`

The file `frequency.py` contains the code used for deriving the sentiment of new terms.


5. Which State is happiest?
------------------------------------------
Assume the tweet file contains data formatted the same way as the livestream data.

There are different ways you might assign a location to a tweet. Here are three:

- Use the coordinates field (a part of the place object, if it exists, to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into a state.
- Use the other metadata in the place field. Much of this information is hand-entered by the twitter user and may not always be present or reliable, and may not typically contain a state name.
- Use the user field to determine the twitter user's home city and state. This location does not necessarily correspond to the location where the tweet was posted, but it's reasonable to use it as a proxy.

You may find it useful to use this [python dictionary of state abbreviations](http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/). In this file, each line is a Tweet object, as [described in the twitter documentation](https://dev.twitter.com/overview/api/tweets). We can ignore any tweets for which you cannot assign a location in the United States. 

Note: Not every tweet will have a text field - again, real data is dirty! Be prepared to debug, and feel free to throw out tweets that your code can't handle to get something working. For example, here we ignore all non-English tweets.

The file `happiest_state.py` contains the code used for deriving the sentiment of new terms.

6. Top ten hash tags
------------------------------------------
Write a Python script top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered in Part 1.
In the tweet file, each line is a Tweet object, as [described in the twitter documentation](https://dev.twitter.com/overview/api/tweets). To find the hashtags, we need not parse the text field; the hashtags have already been extracted by twitter.

The file `top_ten.py` contains the code used for deriving the sentiment of new terms.

##Credits
These instructions were provided as a part of an assignment for the online course 'Introduction to Data Science' on Coursera. You can view the relevant assignment [here](https://class.coursera.org/datasci-002/assignment/view?assignment_id=3).
