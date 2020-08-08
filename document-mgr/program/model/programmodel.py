from program.model.database import Database
from filemngr import FileManager

import configparser


class Model:
    # class variables
    database = None
    file_mgr = None
    document = None

    ##########################################################################
    #
    #
    #

    def __init__(self, configuration):
        self.config = configuration
        self.init_database()
        self.init_file_mgr()

    ##########################################################################
    #
    #
    #

    def init_database(self):
        self.database = Database(self.config["data_file"]["database_file"])

        for key, value in self.config["db_tables"].items():
            self.database.create_table(key, value)

    ##########################################################################
    #
    #
    #

    def init_file_mgr(self):
        self.file_mgr = FileManager(self.config["directory"]["data_folder"])
        self.file_mgr.extract_file_information(self.document)

    ##############################################################################
    #
    # Register a scanned document or an printed document
    #
    # 'register_scanned_document' and 'register_printed_document' are taking a
    # 'file' as input and add the specific file information to the document
    # database. A copy of the file is saved in the folder 'doc/'
    #

    def register_document(self, file_path, code):
        pass

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

    def get_linked_documents(self, link_id):
        pass

    def get_documents_of_set(self, set_id):
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

    def get_document_information(self, doc_id):
        # data = self.database.joined_select("document", "")
        # return data
        pass

    def update_document_information(self, doc_id):
        pass

    ##############################################################################
    #
    # Delete documents of the database and the doc/ folder
    #
    # All three functions delete documents. Either one specific document gets
    # deleted, or two documents of a link connection get deleted or all documents
    # which origin of a specific document get deleted
    #

    def delete_document(self, doc_id):
        pass

    def delete_linked_documents(self, link_id):
        pass

    def delete_documents_of_set(self, set_id):
        pass


config = configparser.ConfigParser()
config.read('../../config.ini')
test = Model(config)
document = "E:\\Bücher\\Chess\\John Nunn - Learn Chess-Gambit Publications (2010).pdf"
document1 = "E:/Bücher/Chess/John Nunn - Learn Chess-Gambit Publications (2010).pdf"
test.register_document(document, "98234792374")
