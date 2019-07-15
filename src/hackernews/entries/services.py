import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List

HACKER_NEWS = 'https://news.ycombinator.com/'


def get_hacker_news() -> List:
    f = urllib.request.urlopen(HACKER_NEWS)
    soap = BeautifulSoup(f, features='html.parser')

    hacker_news = []

    for item in soap.select('a.storylink'):
        hacker_news.append({
            'url': item['href'],
            'title': item.string,
    })
    return hacker_news

