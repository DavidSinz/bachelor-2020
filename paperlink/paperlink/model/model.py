import time

from model.database import Database
from model.filemanager import FileManager


class Model:

    # ==========================================================================
    #
    #
    #

    database = None
    file_mgr = None
    document = None
    db_table = "document"

    # ==========================================================================
    #
    #
    #

    def __init__(self, db_file, data_dir, db_columns):
        self.db_columns = db_columns
        self.database = Database(db_file)
        self.file_mgr = FileManager(data_dir)

    def db_create_table(self, db_table, columns):
        self.database.create_table(db_table, columns)

    # ==========================================================================
    #
    #
    #

    def register_printed_document(self, file_name, path, md5code):
        index = self.check_document_in_database(file_name, path)
        link_id = self.generate_new_link_id()
        set_id = None
        if index == None:
            set_id = self.generate_new_set_id()
            index = 0
        else:
            set_id = self.get_set_id(index)
            index = self.next_index_for_db_table()
        datetime_now = time.strftime('%Y-%m-%d %H:%M:%S')
        values = f"{index}, '{file_name}', '{path}', '{md5code}', {link_id}, {set_id}, 'file_type', 20, 'print', '{datetime_now}', 0, '1234', '1223'"
        self.database.insert(self.db_table, self.db_columns, values)

    def register_scanned_document(self, file_name, path, md5code):
        result = self.database.select(self.db_table, "link_id, set_id", f"code = '{md5code}'")
        if len(result) > 0:
            link_id = result[0][0]
            set_id = result[0][1]
            datetime_now = time.strftime('%Y-%m-%d %H:%M:%S')
            index = self.next_index_for_db_table()
            values = f"{index}, '{file_name}', '{path}', '{md5code}', {link_id}, {set_id}, 'file_type', 20, 'scan', '{datetime_now}', 0, '1234', '1223'"
            self.database.insert(self.db_table, self.db_columns, values)
        else:
            print("The printed version of this document is not registered")
        


    def generate_new_link_id(self):
        result = self.database.select_max(self.db_table, "link_id")[0]
        if result != None:
            return result + 1
        return 0
        

    def generate_new_set_id(self):
        result = self.database.select_max(self.db_table, "set_id")[0]
        if result != None:
            return result + 1
        return 0

    # ==========================================================================
    #
    #
    #

    def next_index_for_db_table(self):
        result = self.database.select_max(self.db_table, "id")
        if len(result) > 0:
            return int(result[0]) + 1
        return 1

    def check_document_in_database(self, file_name, path):
        result = self.database.select(
            self.db_table, "id", f"name = '{file_name}' AND path = '{path}'")
        if len(result) > 0:
            return result[0][0]
        return None

    # ==========================================================================
    #
    #
    #

    def get_all_documents(self):
        #self.database.insert(self.db_table, "id, name, path, code, link_id, set_id, file_type, size, type, insert_date, trash, data_name, screenshot", "1, 'test.pdf', '/example/', 'PL:22:33', 10, 40, 'pdf', 23, 'print', '2020-03-21 15:20:30', 0, 'p00001', 'img12.png'")
        return self.database.select(self.db_table, "*")

    def get_documents(self):
        return self.database.select(self.db_table, "*", "trash = 0")

    def get_one_document(self, doc_id):
        return self.database.select(self.db_table, "*", f"id = {doc_id}")[0]

    def get_print_documents(self):
        return self.database.select(self.db_table, "*", "trash = 0 AND type = 'print'")

    def get_scan_documents(self):
        return self.database.select(self.db_table, "*", "trash = 0 AND type = 'scan'")

    def get_linked_documents(self, doc_id):
        link_id = self.get_link_id(doc_id)
        result = self.database.select(
            self.db_table, "*", f"trash = 0 AND link_id = {link_id}")
        if len(result) < 2:
            result.append(None)
        return result

    def get_documents_of_same_origin(self, doc_id):
        set_id = self.get_set_id(doc_id)
        where_pdocs = f"trash = 0 AND set_id = {set_id} AND type = 'print'"
        print_docs_id = self.database.select(self.db_table, "id", where_pdocs)
        result = []
        for pd_id in print_docs_id:
            linked_docs = self.get_linked_documents(pd_id[0])
            result += linked_docs
            if len(linked_docs) < 2:
                result.append(None)
        return result

    def get_trashed_documents(self):
        return self.database.select(self.db_table, "*", "trash = 1")

    # ==========================================================================
    #
    #
    #

    def update_document_information(self, doc_id, columns, values):
        columns = columns.split(",")
        values = values.split(",")
        for i in range(len(columns)):
            setter = columns[i] + " = " + values[i] + ", "
        setter = setter[:-2]
        self.database.update(self.db_table, setter, f"id = {doc_id}")

    # ==========================================================================
    #
    #
    #

    def get_link_id(self, doc_id):
        return self.database.select(self.db_table, "link_id", f"id = {doc_id}")[0][0]

    def get_set_id(self, doc_id):
        return self.database.select(self.db_table, "set_id", f"id = {doc_id}")[0][0]

    # ==========================================================================
    #
    #
    #

    def recover_document(self, doc_id):
        print(doc_id)
        self.database.update(self.db_table, f"trash=0", f"id = {doc_id}")

    def trash_document(self, doc_id):
        self.database.update(self.db_table, f"trash = 1", f"id = {doc_id}")

    def delete_document(self, doc_id):
        self.database.delete(self.db_table, f"id = {doc_id}")

    # ==========================================================================
    #
    #
    #
