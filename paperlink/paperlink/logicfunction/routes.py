from flask import Flask, Blueprint, redirect, url_for, request

from logicfunction import logicfunc as lfunc

app = Blueprint("logicfunction", __name__)


@app.route('/dump/<string:context>/<int:doc_id>', methods=['POST'])
def dump(context, doc_id):
    lfunc.dump_document(doc_id)
    return redirect(url_for(context))


@app.route('/delete/<int:doc_id>', methods=['POST'])
def delete(doc_id):
    lfunc.delete_document(doc_id)
    return redirect(url_for("presentation.trash"))


@app.route('/update/<string:context>/<int:doc_id>', methods=['POST'])
def update(context, doc_id):
    source_path = request.form['pathInputField']
    lfunc.update_document(doc_id, source_path)
    return redirect(url_for(context))

@app.route('/register_print', methods=['POST'])
def register_print():
    source_path = request.form['printDocPath']
    lfunc.register_print_document(source_path)
    return redirect(url_for("presentation.index"))

@app.route('/register_scan', methods=['POST'])
def register_scan():
    source_path = request.form['scanDocPath']
    lfunc.register_scan_document(source_path)
    return redirect(url_for("presentation.index"))
