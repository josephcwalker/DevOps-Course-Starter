from flask import Flask, render_template, redirect, request

from todo_app.flask_config import Config
from todo_app.data.trello_items import TrelloService
from todo_app.view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    trello_service = TrelloService()

    @app.route('/')
    def index():
        item_view_model = ViewModel(trello_service.get_items())
        return render_template("index.html", view_model=item_view_model)

    @app.route("/new", methods=["POST"])
    def new_todo():
        trello_service.add_item(request.form.get("item"))

        return redirect("/")

    @app.route("/complete", methods=["POST"])
    def complete():
        trello_service.complete_item(request.form.get("id"))

        return redirect("/")

    return app
