import urllib.request
from typing import List

from bs4 import BeautifulSoup
from django.db import IntegrityError

from .models import Entry

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


def add_entries() -> None:
    for item in get_hacker_news():
        try:
            Entry.objects.create(**item)
        except IntegrityError:
            pass