import os
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackernews.settings')

app = Celery('hackernews', broker='redis://localhost:6379')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add_enties_from_celery': {
        'task': 'hackernews.entries.tasks.add_enties_from_celery',
        'schedule': crontab(minute='*/5'),
    },
}

