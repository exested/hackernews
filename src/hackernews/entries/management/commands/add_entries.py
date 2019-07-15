from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ...models import Entry
from ...services import get_hacker_news


class Command(BaseCommand):

    def handle(self, *args, **options):
        for item in get_hacker_news():
            try:
                Entry.objects.create(**item)
            except IntegrityError:
                pass