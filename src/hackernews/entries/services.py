import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

HACKER_NEWS = 'https://news.ycombinator.com/'


def get_hacker_news() -> list:
    f = urllib.request.urlopen(HACKER_NEWS)
    soap = BeautifulSoup(f)

    hacker_news = []

    for item in soap.select('a.storylink'):
        # TODO: get real publish_date from detail news

        hacker_news.append({
            'url': item['href'],
            'title': item.string,
            'publish_date': datetime.now(),
        })
    return hacker_news

