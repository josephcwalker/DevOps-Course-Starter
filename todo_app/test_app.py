import os
from dotenv import load_dotenv, find_dotenv
import requests
from todo_app import app
import pytest

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'test item 1' in response.data.decode()
    assert 'test item 2' in response.data.decode()
    assert 'test item 3' in response.data.decode()


class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def stub(method, url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')

    if method == "GET" and url == f"https://api.trello.com/1/boards/{test_board_id}/cards/all":
        fake_response_data = [
            {
                "id": "123",
                "name": "test item 1",
                "closed": False,
            },
            {
                "id": "456",
                "name": "test item 2",
                "closed": True,
            },
            {
                "id": "789",
                "name": "test item 3",
                "closed": False,
            },
        ]
        return StubResponse(fake_response_data)

    raise Exception(f"Integration test did not expect URL \"{url}\"")
