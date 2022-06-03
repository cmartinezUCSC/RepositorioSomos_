#!/usr/bin/env python3
import json
from requests import Session as request_session
from tqdm import tqdm


session = request_session()


def clean_text(text):
    files = {
        "data": (None, text, "text/plain"),
    }
    response = session.post("http://127.0.0.1:8000/preproc", files=files)
    return response.text


# with open('emoji.json') as io:
#     emojis = json.load(io)['Fully_Qualified']
#     emojis = sorted(emojis, key=len, reverse=True)

# with open('annotations.json') as io:
#     annotations = {}
#     tmp = json.load(io)
#     annotations.update(tmp['Basic'])
#     annotations.update(tmp['Derived'])


# unannotated = set()
# untagged = set()
# tag_dict = defaultdict(list)

# #Este paso debiera pasar
# def replace_emoji(sent, index=0):
#     line = sent['text']
#     line = normalize('NFC', line)
#     for emoji in emojis:
#         if emoji in line and emoji in annotations: #preguntar si estas en el senti_emoji además y sacar la emoción
#             tags = [a for a in annotations[emoji]["tags"] if ' ' not in a]
#             if tags:
#                 line = line.replace(emoji, f' {tags[index]} ')
#                 tag_dict[sent['_id']].append(tags[index])
#                 #Buscar en el archivo sentic_emoji.json
#             else:
#                 untagged.add(emoji)
#         else:
#             unannotated.add(emoji)
#     return line





with open("../senti_emoji.json") as categoriesIO, open(
    "../tweet_download/all.json"
) as tweetsIO:
    categories = json.load(categoriesIO)
    tweet_list = json.load(tweetsIO)

for tweet in tqdm(tweet_list):
    senti = set()
    tweet = tweet["text"].strip()
    for emotion, emoji_list in categories.items():
        if any(emoji in tweet for emoji in emoji_list): 
            senti.add(emotion)
    if len(senti) == 1:
        senti = sorted(senti)
        tweet = clean_text(tweet).strip()
        tweet = " ".join(tweet.split("\n"))
        senti_tags = [f"__label__{s}" for s in senti]
        if len(tweet):
            print(f"{' '.join(senti_tags)} {tweet}")
