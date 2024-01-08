""" Use the NewsAPI and the requests module to fetch the daily news related to different topics
    Go to : https://newsapi.org/ and explore the various options to build your application """

import requests
import json

Query=input("what type of news are you interested in: ")
url=f"https://newsapi.org/v2/everything?q={Query}&from=2023-11-30&sortBy=publishedAt&apiKey=17b2f6530dae4c40afbfcd653aebe327 "
r=requests.get(url)
# print(r.text)       op:- This will print the news in text format I want in jayson format
news=json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])       # So many news are printing at a time to know when one news is ended,
    print("---------------------------------------")
   
















