# Twitter_API_project  -- Arcane Analysis

![Arcane](https://user-images.githubusercontent.com/64421607/144581081-fffa2056-0a33-4dc7-bd33-3918e7bac557.JPG)

# Description

I discovered in a Kaggle topic the "sentiment analysis" about the vaccination (https://www.kaggle.com/gpreda/explore-vaccines-tweets/notebook)
and I decided do the same thing on the Netflix's serie Arcane.

Firstly, I would have liked to take all the tweets between the first and the last episode but finally I did the analysis on the last 30k tweets on the 02/12/2021.
(Twitter API was asking much informations to get the elevation it needed to the first case, so I gived up and go to the second case).

## Scrapping 

I used the twitter API (https://developer.twitter.com/en/portal/dashboard) and tweepy to get the 30k Tweets.
If you want do the same : 

If you want to use this project : 

 1 - You need to create your own project on the developer twitter portal and get your API keys and tokens :

        `API_KEY=""`

        `API_KEY_SECRET=""`

        `BEARER_TOKEN=""`

        `ACCESS_TOKEN=""`

        `ACCESS_TOKEN_SECRET=""`

2 - Put your key and token info in the "bot_info.txt" file

3 - You can now configure your own query with the "twitter_bot.py" file 


