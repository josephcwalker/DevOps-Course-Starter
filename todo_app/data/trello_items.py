import requests
import os
import logging

LIST_ID = os.getenv("TRELLO_LIST_ID")

API_PARAMS = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
}

TRELLO_API_URL = "https://api.trello.com/1"

def _card_from_trello_card(trello_card):
    return {
        "id": trello_card.get("id"),
        "status": "Not Started",
        "title": trello_card.get("name"),
    }

def get_items():
    response = requests.request(
        "GET",
        f"{TRELLO_API_URL}/lists/{LIST_ID}/cards",
        params=API_PARAMS,
    )
    
    cards = map(_card_from_trello_card, response.json())
    return cards

def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def add_item(title):
    requests.request(
        "POST",
        f"{TRELLO_API_URL}/cards",
        params={
            "idList": LIST_ID,
            "name": title,
            **API_PARAMS,
        },
    )

def save_item(item):
    requests.request(
        "PUT",
        f"{TRELLO_API_URL}/cards/{item["id"]}",
        params={
            "name": item["title"],
            **API_PARAMS,
        },
    )

def complete_item(id):
    logging.error(id)
    response = requests.request(
        "PUT",
        f"{TRELLO_API_URL}/cards/{id}",
        params={
            "closed": "true",
            **API_PARAMS,
        },
    )

    logging.error(response.content)
