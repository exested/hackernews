import pytest
from ..services import get_hacker_news


@pytest.mark.django_db
def test_get_hacker_news():

    result = get_hacker_news()

    assert result[0]['url']
    assert result[0]['title']
