from model.database import Database
from model.filemanager import FileManager


class Model:

    #==========================================================================
    #
    #
    #
    
    database = None
    file_mgr = None
    document = None
    db_table = "document"

    #==========================================================================
    #
    #
    #

    def __init__(self, db_file, data_dir):
        self.database = Database(db_file)
        self.file_mgr = FileManager(data_dir)

    def db_create_table(self, db_table, columns):
        self.database.create_table(db_table, columns)

    #==========================================================================
    #
    #
    #
    
    def process_code(self, code):
        return {"link_id": code.split(":")[1], "set_id": code.split(":")[2]}

    def register_document(self, data):
        print("hey was geht ab")
        #file_name = ""
        #index = self.database.select_max(self.db_table, "id")
        #if index is None:
        #    index = "0"
        #else: index = str(int(index[0]) + 1)
        #data_file = data_file[:-len(index)] + index
        #file_data = {"id": index, "path": file_path, "code": code}
        #print(file_data)
        #print(self.process_code(code))
        #print(self.file_mgr.extract_file_information(file_path))
        #file_data = {**file_data, **self.process_code(code)
        ##, **self.file_mgr.extract_file_information(file_path)
        #}
        #columns = ', '.join(file_data.keys())
        #values = "'" + ("', '".join(file_data.values())) + "'"
        #self.database.create_table(self.db_table, columns)
        #self.database.insert(self.db_table, columns, values)
        ##self.file_mgr.save_file_to_data_dir(file_path, data_file)
    
    def register_printed_document(self, data):
        self.register_document(data)
    
    def register_scanned_document(self):
        pass

    #==========================================================================
    #
    #
    #

    def get_linked_documents(self, link_id):
        if link_id is not None:
            return self.database.select(self.db_table, "*", "link_id = '" + link_id + "'")
        print('no link id defined')

    def get_documents_of_set(self, set_id):
        if set_id is not None:
            return self.database.select(self.db_table, "*", "set_id = '" + set_id + "'")
        print('no set id defined')

    #==========================================================================
    #
    #
    #

    def get_document_information(self, doc_id=None):
        #self.database.insert(self.db_table, "id, name, path, code, link_id, set_id, file_type, size, type, data_name, screenshot", "1, 'test.pdf', '/example/', 'PL:22:33', 22, 33, 'pdf', 23, 'print', 'p00001', 'img12.png'")
        if doc_id is None:
            return self.database.select(self.db_table, "*")
        return self.database.select(self.db_table, "*", "id = '"+ str(doc_id)+ "'")

    def update_document_information(self, doc_id):
        pass

    #==========================================================================
    #
    #
    #

    def delete_document(self, doc_id):
        self.database.delete(self.db_table, "id = '" + str(doc_id)+"'")

    def delete_linked_documents(self, link_id):
        pass

    def delete_documents_of_set(self, set_id):
        pass

