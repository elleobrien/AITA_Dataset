import praw
import pandas as pd
import csv
import json

# Read in the list of post ids
df = pd.read_csv("post_ids_and_scores.csv")
# Filter only posts with 3+ upvotes
df_use = df[df['score'] >= 3]
use_posts = df_use['id'].tolist()

# Read my keys
with open("keys.json") as f:
    keys = json.load(f)

# Initialize reddit API
reddit = praw.Reddit(client_id=keys['client_id'],
                     client_secret=keys['client_secret'],
                     user_agent=keys['user_agent'])

# For each post in the list, get the data we care about
title_list = list()
text_list = list()
edited_list = list()
verdict_list = list()

f = open('subreddit_posts_text.csv',"w") 
writer = csv.writer(f, quoting=csv.QUOTE_ALL)

counter = 0
for idx in use_posts:
    post = reddit.submission(idx)
    title = post.title
    text = post.selftext
    edited = str(post.edited)
    verdict = post.link_flair_text 
    if not verdict:
        verdict =  "NA" 

    line_stuff = [idx,title,text,edited,verdict]
    writer.writerow(line_stuff)

    if counter % 1000 == 0:
        print(counter)
    counter += 1

f.close()

