# import custom modules
import output
from database import Database
from document import Document

# create an instance of the class Document for managing documents and also
# create an instance of the class Database for managing database queries
document = Document()
database = Database('document-manager')


##############################################################################
#
# Register a scanned document or an printed document
#
# 'register_scanned_document' and 'register_printed_document' take a
# file_name as input and add the specific file information to the document
# database. A copy of the file is saved in the folder 'docs/'
#

def register_scanned_document(file_name):
    document.register(file_name)


def register_printed_document(file_name):
    document.register(file_name)


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
    document.get_linked_document_ids(link_id)


def get_documents_of_set(set_id):
    document.get_document_ids_of_set(set_id)


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

def get_document_information(doc_id):
    document.get_document_information(doc_id)


def update_document_information(doc_id, data):
    document.update_document_information(doc_id, data)


##############################################################################
#
# Delete documents of the database and the doc/ folder
#
# All three functions delete documents. Either one specific document gets
# deleted, or two documents of a link connection get deleted or all documents
# which origin of a specific document get deleted
#

def delete_document(doc_id):
    document.delete_document(doc_id)


def delete_linked_documents(link_id):
    document.delete_linked_documents(link_id)


def delete_documents_of_set(set_id):
    document.delete_documents_of_set(set_id)
