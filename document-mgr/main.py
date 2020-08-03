##############################################################################
#
# Implemented with: Python 3.7
# Used modules: logging, pathlib, sqlite3, sys
#

from sys import argv
import configparser

from database import Database
from filemngr import FileMngr

##############################################################################
#
# create an instance of the class Document for managing document files and
# information and also create an instance of the class Database for managing
# database queries
#

config = configparser.ConfigParser()
config.read('config.ini')

data_dir = FileMngr(config["directory"]["data_folder"])
database = Database(config["data_file"]["database_file"])


##############################################################################
#
# Register a scanned document or an printed document
#
# 'register_scanned_document' and 'register_printed_document' are taking a
# 'file' as input and add the specific file information to the document
# database. A copy of the file is saved in the folder 'doc/'
#


def register_printed_document(file, code):
    doc_id = database.select_max("document", "id")[0]
    p_doc_id = database.select_max("printed_doc", "id")[0]
    if doc_id is None:
        doc_id = 0
    else:
        doc_id += 1
    if p_doc_id is None:
        p_doc_id = 0
    else:
        p_doc_id += 1
    database.insert("document", config["db_columns"]["document"], f"{doc_id}, '{code}', 6, 5, '{file}', 'path', 'date'")
    database.insert("printed_doc", config["db_columns"]["printed_doc"], f"{p_doc_id}, {doc_id}")
    file_name = "p" + str(p_doc_id)
    data_dir.save(file, file_name)


def register_scanned_document(file, code):
    doc_id = database.select_max("document", "id")[0]
    s_doc_id = database.select_max("scanned_doc", "id")[0]
    if doc_id is None:
        doc_id = 0
    else:
        doc_id += 1
    if s_doc_id is None:
        s_doc_id = 0
    else:
        s_doc_id += 1
    database.insert("document", config["db_columns"]["document"], f"{doc_id}, '{code}', 6, 5, '{file}', 'path', 'date'")
    database.insert("scanned_doc", config["db_columns"]["scanned_doc"], f"{s_doc_id}, {doc_id}")
    file_name = "s" + str(s_doc_id)
    data_dir.save(file, file_name)


##############################################################################
#
# Get the documents which are in relation to each other
#
# 'get_linked_document': This returns two documents which are linked to each
# other. When printing a file, a document gets an 'link_id'. If this
# printed document is scanned again, then this link_id creates a connection
# between scan and print version of a document. This function returns both
# linked documents.
#
# 'get_documents_of_set': This returns all documents which are from the same
# origin. When printing a document and scanning a document multiple times,
# many different versions of a document will be created. They are all saved
# as set in the database. This function returns a list of them.
#

def get_linked_document(link_id):
    # database_data = database.select_ids_of_linked_documents(db_select)
    # document_data = document.get_of_linked_documents(link_id)
    pass


def get_documents_of_set(set_id):
    # document.get_document_ids_of_set(set_id)
    pass


##############################################################################
#
# Retrieve and change information about a document
#
# 'get_document_information': This returns information stored in a database
# about a document. When a document is registered, an entry with document
# information will be created in the database. This function returns this
# information.
#
# 'update_document_information': This updates the document information to an
# document entry in the database. The information, which will be given in the
# data parameter, is an python dictionary and will be used to change specific
# information fields of this document.
#

def get_document_information(doc_id, db_data):
    # document.get_document_information(doc_id)
    # return database.select(db_data)
    pass


def update_document_information(doc_id, db_data):
    # document.update_document_information(doc_id)
    # database.update(db_data)
    pass


##############################################################################
#
# Delete documents of the database and the doc/ folder
#
# All three functions delete documents. Either one specific document gets
# deleted, or two documents of a link connection get deleted or all documents
# which origin of a specific document get deleted
#

def delete_document(doc_id, db_data):
    # document.delete_document(doc_id)
    database.delete(db_data)


def delete_linked_documents(link_id):
    # document.delete_linked_documents(link_id)
    pass


def delete_documents_of_set(set_id):
    # document.delete_documents_of_set(set_id)
    pass


##############################################################################
#
# Main method which handles the all running processes
#

def main(args):
    for key, value in config["db_tables"].items():
        database.create_table(key, value)

    register_printed_document("test/example.pdf", "DL-L:123-S:343")
    # print(get_document_information(0, db_select))
    # update_document_information(0, db_update)
    # delete_document(0, db_delete)
    # print(get_document_information(0, db_select))

    # data_dir.save("test/example.jpg", "test")
    # data_dir.delete("test")

    # database.insert("document", "id, code, file_name, path, insert_date", "0, 12312, 'test.py', 'sfd', 'sdfs'")
    # database.update("document", "id = 5", "id = 32")
    # database.delete("document", "id = 5")
    # print(database.select("document", "*"))


if __name__ == "__main__":
    main(argv[1:])
