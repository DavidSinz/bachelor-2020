from flask import Flask, Blueprint

from datamanager import main

app = Blueprint("datamanager", __name__)


print(main.get_all_documents())

@app.route("/get_full_table")
def index():
    return "datamanager"
