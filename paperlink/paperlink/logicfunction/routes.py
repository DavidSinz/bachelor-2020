from flask import Flask, Blueprint

app = Blueprint("logicfunction", __name__)


@app.route("/logicfunction")
def index():
    return "logicfunction"
