import requests
from flask import Flask, Blueprint, render_template, request

app = Blueprint("presentation",
                __name__,
                template_folder="templates",
                static_folder="static",
                static_url_path="/presentation/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/all_docs")
def all_docs():
    data = get_document_data("all")
    return render_template("view_docs.html", documents=data)


@app.route("/print_docs")
def print_docs():
    data = get_document_data("print")
    return render_template("view_docs.html", documents=data)


@app.route("/scan_docs")
def scan_docs():
    data = get_document_data("scan")
    return render_template("view_docs.html", documents=data)


@app.route('/doc_info')
def doc_info():
    data = get_document_data("info")
    return render_template('doc_info.html', documents=data)


@app.route('/trash')
def trash():
    data = get_document_data("dumped")
    return render_template("trash.html", documents=data)


@app.route('/update')
def update():
    return render_template("update.html")


@app.route('/help')
def help():
    return render_template("help.html")


def get_document_data(doc_type="all"):
    if doc_type == "all":
        token = "all_documents"
    elif doc_type == "print":
        token = "print_documents"
    elif doc_type == "scan":
        token = "scan_documents"
    elif doc_type == "info":
        token = "doc_information"
    elif doc_type == "dumped":
        token = "dumped_documents"
    url = request.host_url + token
    result = requests.post(url)
    return result.json()
