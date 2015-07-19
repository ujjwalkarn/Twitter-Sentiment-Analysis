This repository contains the codes for carrying out sentiment analysis on Twitter livestream data. 

As a part of this project, we can do the following:

- Access Twitter live stream and captured tweets using the oauth2 library and Twitter REST API.
- Parse raw tweets obtained in JavaScript Object Notation.
- Compute term frequency histogram of the livestream data for calculating tweet sentiments.
- Query the raw tweet data for various parameters of interest like hashtags, origin of the tweet.
- Find top ten hashtags across the tweet data.

1. Get Twitter Data
-------------------
To access the live stream, you will need to install the oauth2 library so you can properly authenticate.
```
$ pip install oauth2
```
The steps below will help you set up your twitter account to be able to access the live stream.

1. Create a twitter account if you do not already have one.
2. Go to https://dev.twitter.com/apps and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5. On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
6. Click the button "Create My Access Token". You can Read more about Oauth authorization.
7. You will now copy four values into `twitterstream.py`. These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". All four should now be visible on the API Keys page. (You may see "API Key" referred to as "Consumer key" in some places in the code or on the web; they are synonyms.) 
8. Open `twitterstream.py` and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:
  - api_key = "<Enter api key>"
  - api_secret = "<Enter api secret>"
  - access_token_key = "<Enter your access token key here>"
  - access_token_secret = "<Enter your access token secret here>"
9. Run the following and make sure you see data flowing and that no errors occur `$ python twitterstream.py > output.txt`
10. This command pipes the output to a file. Stop the program with Ctrl-C, but wait at least 3 minutes for data to accumulate.
11. If you wish, modify the file to use the twitter search API to search for specific terms. For example, to search for the term "microsoft", you can pass the following url to the twitterreq function: `https://api.twitter.com/1.1/search/tweets.json?q=microsoft`
