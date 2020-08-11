from flask import Flask, Blueprint, request, jsonify

from logicfunction import main

app = Blueprint("logicfunction", __name__)


"""id, name, path, size, type, dumped, screenshot"""

all_documents = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"},
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "scan", "dumped": 0, "screenshot": "/home/david/test.jpg"},
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"}
]

print_documents = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"},
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "print", "dumped": 0, "screenshot": "/home/david/test.jpg"}
]

scan_documents = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "scan", "dumped": 0, "screenshot": "/home/david/test.jpg"}
]

dumped_documents = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "scan", "dumped": 0, "screenshot": "/home/david/test.jpg"}
]

doc_information = [
    {"id": 0, "name": "test.py", "path": "/example/", "size": "50 MB",
        "type": "scan", "dumped": 0, "screenshot": "/home/david/test.jpg"}
]


@app.route('/all_documents', methods=['POST'])
def get_all_documents():
    return jsonify(all_documents)


@app.route('/print_documents', methods=['POST'])
def get_print_documents():
    return jsonify(print_documents)


@app.route('/scan_documents', methods=['POST'])
def get_scan_documents():
    return jsonify(scan_documents)


@app.route('/doc_information', methods=['POST'])
def get_doc_information():
    return jsonify(doc_information)


@app.route('/dumped_documents', methods=['POST'])
def get_dumped_documents():
    return jsonify(dumped_documents)
