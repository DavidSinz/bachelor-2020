"""PaperLink

This script allows the user to make printed documents identifiable. A small 
qr code is added to every document, that will be printed out. When the user 
scans this paper document, the qr code will be identified by the program and 
the scan file can be traced back to it's original digital file. 
"""

from flask import Flask, render_template, Response, request, redirect, url_for
import os


"""id, name, path, size, type, dumped, screenshot"""

documents = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"},
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "scan", "dumped": 0, "screenshot": "/home/david/test.jpg"},
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"},
]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/all_docs")
def all_docs():
    return render_template("view_docs.html", documents=documents)


@app.route("/print_docs")
def print_docs():
    return render_template("view_docs.html", documents=documents)


@app.route("/scan_docs")
def scan_docs():
    return render_template("view_docs.html", documents=documents)


@app.route('/doc_info')
def doc_info():
    return render_template('doc_info.html')


@app.route('/trash')
def trash():
    return render_template("trash.html", documents=documents)


@app.route('/update')
def update():
    return render_template("update.html")


@app.route('/help')
def help():
    return render_template("help.html")


if __name__ == '__main__':
    app.run(debug=True)
