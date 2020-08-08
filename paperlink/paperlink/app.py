from flask import Flask, render_template, Response, request
import os
import configparser

from model.model import Model
from controller.forms import DocumentForm


app = Flask(__name__, template_folder="view/")

config = configparser.ConfigParser()
config.read(os.path.join(app.root_path, 'config.ini'))

database = os.path.join(app.root_path, 'db', 'document.db')
data_dir = os.path.join(app.root_path, 'data')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_docs', methods=['GET', 'POST'])
def view_docs():
    model = Model(database, data_dir)
    model.db_create_table("document", config['DATABASE']['dbcreatetable'])
    docs = model.get_document_information()
    return render_template("view_docs.html", documents=docs)

@app.route('/doc_info')
def doc_info():
    documents = ["hey", "was", "geht"]
    return render_template('doc_info.html', documents=documents)

@app.route('/update')
def update():
    return render_template("update.html")

@app.route('/help')
def help():
    return render_template("help.html")

if __name__ == '__main__':
    app.run(debug=True)
