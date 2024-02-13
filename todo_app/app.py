from flask import Flask, render_template, redirect, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template("index.html", items=get_items())

@app.route("/new", methods=["POST"])
def new_todo():
    add_item(request.form.get("item"))

    return redirect("/")
