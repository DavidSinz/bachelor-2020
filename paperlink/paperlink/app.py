"""PaperLink

This script allows the user to make printed documents identifiable. A small 
qr code is added to every document, that will be printed out. When the user 
scans this paper document, the qr code will be identified by the program and 
the scan file can be traced back to it's original digital file. 
"""

from flask import Flask, render_template, Response, request, redirect, url_for
import os
import configparser

from model.model import Model
from controller.forms import UpdateDocForm


app = Flask(__name__, template_folder="view/")

config = configparser.ConfigParser()
config.read(os.path.join(app.root_path, 'config.ini'))

database = os.path.join(app.root_path, 'db', 'document.db')
data_dir = os.path.join(app.root_path, 'data')


@app.route('/')
def index():
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    return render_template('index.html')


@app.route('/view_docs/<string:context>', methods=['GET', 'POST'])
@app.route('/view_docs/<string:context>/<int:del_id>', methods=['GET', 'POST'])
def view_docs(context="all", del_id=None):
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    if del_id != None:
        model.trash_document(del_id)
    if context == "print":
        docs = model.get_print_documents()
    elif context == "scan":
        docs = model.get_scan_documents()
    else:
        docs = model.get_documents()
    return render_template("view_docs.html", documents=docs, context=context)


@app.route('/doc_info/<int:doc_id>')
def doc_info(doc_id):
    print("hey")
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    linked_docs = model.get_linked_documents(doc_id)
    docs_of_set = model.get_documents_of_same_origin(doc_id)
    return render_template('doc_info.html', linked_docs=linked_docs, docs_of_set=docs_of_set)


@app.route('/trash', methods=['GET', 'POST'])
@app.route('/trash/<int:del_id>', methods=['GET', 'POST'])
@app.route('/trash/<int:rec_id>', methods=['GET', 'POST'])
def trash(del_id=None, rec_id=None):
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    if del_id != None:
        model.delete_document(del_id)
    if rec_id != None:
        model.recover_document(rec_id)
    docs = model.get_trashed_documents()
    return render_template("trash.html", documents=docs)


@app.route('/update/<string:context>/<int:doc_id>', methods=["GET", "POST"])
def update(context, doc_id):
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    form = UpdateDocForm(request.form)
    if request.method == 'POST' and form.validate():
        model.update_document_information(
            doc_id, "file_name, path, size", f"{form.file_name.data}, {form.path.data}, {form.size.data}")
        return redirect(url_for('view_docs', context=form.context))
    doc = model.get_one_document(doc_id)
    return render_template("update.html", form=form, context=context, f_val=doc[1], p_val=doc[2], s_val=doc[7])


@app.route('/help')
def help():
    return render_template("help.html")


@app.route("/register_printout", methods=['GET', 'POST'])
def register_printout():
    model = Model(database, data_dir, config['DATABASE']['dbcolumns'])
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    file_name = request.args.get('file_name')
    print(file_name)
    #model.register_printed_document(file_name, path, code)
    return 0


if __name__ == '__main__':
    app.run(debug=True)
