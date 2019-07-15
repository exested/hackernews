import pytest


class TestEntryList:
    def test_get(self, client):
        response = client.get('/posts')

        assert response.status_code == 200

