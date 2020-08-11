from flask import Flask, Blueprint

app = Blueprint("datamanager", __name__)


@app.route("/datamanager")
def index():
    return "datamanager"
