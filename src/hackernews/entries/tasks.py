from .services import add_entries
from ..celery import app


@app.task
def add_enties_from_celery():
    add_entries()
