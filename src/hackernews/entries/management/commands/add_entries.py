from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ...models import Entry
from ...services import add_entries


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_entries()