import tweepy
import pandas as pd
from tqdm import tqdm

# Get the token information from the txt file
def get_info_twitter(credential):
    cred_dict = {}
    with open("C:\\Users\\chris\\PycharmProjects\\Webscarping\\bot_info.txt") as f:
        for line in f.read().split('\n'):
            cred_dict[line.split("=")[0]] = line.split("=")[1]
        return cred_dict[credential]


b_token = get_info_twitter("BEARER_TOKEN")
client = tweepy.Client(bearer_token=b_token)

# Replace with your own search query
query = '(arcane OR jinx OR vi OR viktor OR jayce OR silco) -is:retweet  lang:en '

text_list = []
id_list = []
created_at_list = []
source_list = []
lang_list = []
username_list = []
geo_list = []
name_list = []
text_list_pp = []
database = []

# Tweet search on the last 30000 tweet about the query
for tweet in tqdm(tweepy.Paginator(client.search_recent_tweets,
                                   query=query,
                                   tweet_fields=['text', 'author_id', 'created_at', 'geo', 'source', 'lang'],
                                   expansions=['author_id', 'geo.place_id'], max_results=100).flatten(30000)):

    text_list.append(tweet.text)
    id_list.append(tweet.author_id)
    created_at_list.append(tweet.created_at)
    geo_list.append(tweet.geo)
    source_list.append(tweet.source)
    lang_list.append(tweet.lang)

# Some pre-processing for the csv file.
for text in text_list:
    new_text = text.replace(",", " ")
    new_text = text.replace("\n", " ")
    text_list_pp.append(new_text)

print(text_list)
print(text_list_pp)

arcane = pd.DataFrame(list(zip(text_list_pp, id_list, created_at_list, geo_list, source_list, lang_list)),
                      columns=['text', 'user_id', 'created_at', 'country', 'tweet_source', 'language'])

print(arcane)

# Create the CSV result
arcane.to_csv(r"C:\Users\chris\PycharmProjects\Webscarping\arcane.csv")
