##############################################################################
#
# Implemented with: Python 3.7
# Used modules: logging, pathlib, sqlite3, sys
#

# import built in modules
from sys import argv

# import custom modules
from document import Document
from database import Database
from file_mgr import FileManager

# file names which are used in the program
DB_FILE = "document_manager.db"
LOG_FILE = "document-manager.log"

# directories to store files
DOCUMENT_DIRECTORY = "doc/"
DATABASE_DIRECTORY = "db/"
LOG_FILE_DIRECTORY = "log/"

# returned values of database and document methods
document_data = None
database_data = []

##############################################################################
#
# Database information
#
# The following variables are used to interact with the database. They are
# dictionaries with keys as table names and the values as information for
# database manipulation purposes.
#
# 'db_create' is used to create the following three tables:
# - Table 'document': This table stores most of the information of a document
# - Table 'printed_document': This table stores information about printed
#   documents. It uses also data from 'document' and uses therefor a foreign.
#   key from 'document'.
# - Table 'scanned_document': This table stores information about scanned
#   documents. It uses also data from 'document' and uses therefor a foreign
#   key from 'document'.
#
# 'db_insert'
#

db_create = {
    "document": [
        "id INT PRIMARY KEY",
        "code INT",
        "file_name VARCHAR(50)",
        "path VARCHAR(50)",
        "insert_date DATETIME"
    ],
    "printed_document": [
        "id INT PRIMARY KEY",
        "document_id INT"
    ],
    "scanned_document": [
        "id INT PRIMARY KEY",
        "document_id INT"
    ]
}
db_insert = {
    "document": {"id": "0", "code": "123", "file_name": "'test.py'", "path": "'/test/'", "insert_date": "'hey'"},
    "printed_document": {"id": "0", "document_id": "0"}
}
db_select = {
    "document": {"column": ["*"]},
    "printed_document": {"column": ["id"], "where": "id = 0"}
}
db_update = {
    "document": {
        "set": {"id": "100", "path": "'jksdhfkjsd'"},
        "where": "id = 0"
    },
    "printed_document": {
        "set": {"document_id": "3"}
    }
}
db_delete = {
    "document": {},
    "printed_document": {"where": "id = 0"}
}

##############################################################################
#
# create an instance of the class Document for managing document files and
# information and also create an instance of the class Database for managing
# database queries
#

document = Document()
database = Database(DATABASE_DIRECTORY + DB_FILE, db_create)
file_mgr = FileManager(DOCUMENT_DIRECTORY)


##############################################################################
#
# Register a scanned document or an printed document
#
# 'register_scanned_document' and 'register_printed_document' take a
# file_name as input and add the specific file information to the document
# database. A copy of the file is saved in the folder 'doc/'
#


def register_printed_document(file_name):
    document.save_printed_document(file_name)
    db_data = document.get_
    database.insert(db_data)


def register_scanned_document(file_name, db_data):
    document.save_scanned_document(file_name)
    # database.insert(db_data)


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
    # register_printed_document("fdsf", db_insert)
    # print(get_document_information(0, db_select))
    # update_document_information(0, db_update)
    # delete_document(0, db_delete)
    # print(get_document_information(0, db_select))

    # file_mgr.save("test/example.jpg", "test")
    # file_mgr.delete("test")
    pass


if __name__ == "__main__":
    main(argv[1:])
