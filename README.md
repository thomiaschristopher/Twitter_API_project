# Twitter_API_project  -- Arcane Analysis

![Arcane](https://user-images.githubusercontent.com/64421607/144581081-fffa2056-0a33-4dc7-bd33-3918e7bac557.JPG)

# Description

I discovered in a Kaggle topic the "sentiment analysis" about the vaccination (https://www.kaggle.com/gpreda/explore-vaccines-tweets/notebook)
and I decided do the same think on the Netflix's serie Arcane.

Firstly, I would scrap all the tweets between the first and the last episode but finally I just do the analysis on the last 30k tweets on the 02/12/2021.

## Scrapping 

I used the twitter API (https://developer.twitter.com/en/portal/dashboard) and tweepy to get the 30k Tweets.
You need to get your API key and token thanks to it :

`* API_KEY=HXyrc3CVDmGZrzKo09Qm4Agmj
API_KEY_SECRET=78A3rvfBzhCNx76TMOyFeo6WghywiPD8dLpEgP89C8896tHKWO
BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAAzSWAEAAAAA4H%2FquBFucI2Y6qTo4EGzzJelbgE%3DUF8mLJZLvxcwso8BdeVrQ1wIsh7U47M9NkW8k4fLgaToRganVg
ACCESS_TOKEN=930553274-ApQpp51fCf2zgozqMFAPPtmNvC9ySjSNbMenI5Ju
ACCESS_TOKEN_SECRET=AJ1oCS5ho2VSjE5rdiDT1uMmNVC3bxmis9q9D3P1MLe9Y`
