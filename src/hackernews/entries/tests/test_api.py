import pytest
from hackernews.entries.models import Entry


class TestEntryList:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get('/posts')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_with_limit_offset_order(self, client):
        response = client.get('/posts?limit=1&offset=1&order=title')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_json_format(self, client):
        entry = Entry.objects.create(
            title='Entry 1',
            url='https://yandex.ru',
        )

        response = client.get('/posts')
        json = response.json()

        assert json['entry_list'][0]['id'] == entry.id
        assert json['entry_list'][0]['title'] == 'Entry 1'
        assert json['entry_list'][0]['url'] == 'https://yandex.ru'
        assert json['entry_list'][0]['created'] == entry.created.isoformat()
        assert json['total_count']
