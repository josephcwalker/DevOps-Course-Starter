import requests
import os

class Item:
    def __init__(self, id, name, status = "Not Started"):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls(card["id"], card["name"])

class TrelloService:
    def __init__(self):
        self.LIST_ID = os.getenv("TRELLO_LIST_ID")

        self.API_PARAMS = {
            "key": os.getenv("TRELLO_API_KEY"),
            "token": os.getenv("TRELLO_API_TOKEN"),
        }

        self.TRELLO_API_URL = "https://api.trello.com/1"

    def get_items(self):
        response = requests.request(
            "GET",
            f"{self.TRELLO_API_URL}/lists/{self.LIST_ID}/cards",
            params=self.API_PARAMS,
        )

        cards = map(Item.from_trello_card, response.json())
        return cards

    def get_item(self, id):
        items = self.get_items()
        return next((item for item in items if item.id == int(id)), None)

    def add_item(self, title):
        requests.request(
            "POST",
            f"{self.TRELLO_API_URL}/cards",
            params={
                "idList": self.LIST_ID,
                "name": title,
                **self.API_PARAMS,
            },
        )

    def save_item(self, item):
        requests.request(
            "PUT",
            f"{self.TRELLO_API_URL}/cards/{item.id}",
            params={
                "name": item.title,
                **self.API_PARAMS,
            },
        )

    def complete_item(self, id):
        requests.request(
            "PUT",
            f"{self.TRELLO_API_URL}/cards/{id}",
            params={
                "closed": "true",
                **self.API_PARAMS,
            },
        )
