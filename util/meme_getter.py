import requests
import json


def meme_urls(amount: int):
    response = requests.get("https://meme-api.com/gimme/" + str(amount))
    memes = json.loads(response.content)["memes"]
    urls = []
    for meme in memes:
        urls.append(meme["url"])
    return urls
