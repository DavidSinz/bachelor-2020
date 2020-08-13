import requests
from flask import Flask, Blueprint, render_template, request

from logicfunction import logicfunc as lfunc

app = Blueprint("presentation", __name__,
                template_folder="templates",
                static_folder="static",
                static_url_path="/presentation/static")


@app.route("/")
def index():
    #lfunc.register_print_document("/media/david/Volume/Bachelorarbeit/Literatur Recherche/Bachelorarbeiten Beispiele/BA_Baulig F.pdf")
    #lfunc.register_scan_document("/media/david/Volume/Bachelorarbeit/Literatur Recherche/Bachelorarbeiten Beispiele/BA_Baulig F.pdf", "PL:2:0")
    #lfunc.get_entity_linkage_by_doc_id(1)
    #print(lfunc.get_version_history_by_doc_id(0))
    return render_template("index.html")


@app.route("/all_docs")
def all_docs():
    data = lfunc.get_all_documents_presentation()
    return render_template("view_docs.html", documents=data)


@app.route("/print_docs")
def print_docs():
    data = lfunc.get_print_documents_presentation()
    return render_template("view_docs.html", documents=data)


@app.route("/scan_docs")
def scan_docs():
    data = lfunc.get_scan_documents_presentation()
    return render_template("view_docs.html", documents=data)


@app.route('/doc_info/<int:doc_id>')
def doc_info(doc_id):
    data = lfunc.get_doc_information_presentation(doc_id)
    return render_template('doc_info.html', documents=data)


@app.route('/trash')
def trash():
    data = lfunc.get_dumped_documents_presentation()
    return render_template("trash.html", documents=data)


@app.route('/help')
def help():

    return render_template("help.html")
