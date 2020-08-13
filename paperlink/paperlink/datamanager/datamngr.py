"""DataManager

This is the DataManager. Here will be all the files be stored and accessable
for using purposes
"""

import os
import sys
import ast
import getopt

from shutil import copyfile
from flask import Flask, Blueprint, request

from datamanager.database import Database

app = Blueprint("datamanager", __name__,
                static_folder="data",
                static_url_path="/datamanager/data")


class DataManager:

    # Database information
    db_path = "/db/"
    db_name = "document.db"
    db_table = "document"
    db_create = """id           INT             PRIMARY KEY, 
                name            VARCHAR(255)    NOT NULL, 
                path            VARCHAR(4096), 
                code            VARCHAR(255)    NOT NULL, 
                link_id         INT,
                set_id          INT,
                size            INT, 
                type            VARCHAR(8)      NOT NULL, 
                insert_date     DATETIME        NOT NULL, 
                dumped          INT             NOT NULL, 
                data_name       VARCHAR(255), 
                file_type       VARCHAR(20)"""
    db_cols = """id, name, path, code, link_id, set_id, size, type, 
              insert_date, dumped, data_name, file_type"""

    # Data directory information
    doc_dir = "/doc/"
    img_dir = "/img/"

    def __init__(self):
        self.data_path = app.static_folder
        self.database = Database(self.data_path + self.db_path + self.db_name)
        self.database.create_table(self.db_table, self.db_create)

    def save_document(self, data):
        try:
            if not isinstance(data, dict):
                raise Exception
        except Exception as e:
            print(f"Input data is not valid. Should be a dict:\n{e}")
        else:
            columns = ""
            values = ""
            for key, val in data.items():
                if key in self.db_cols:
                    columns += key + ", "
                    if type(val) == str:
                        values += "'" + val + "', "
                    else:
                        values += str(val) + ", "
                else:
                    print(f"'{key}' is not supported by table '{self.db_table}'")
            if len(columns) > 0:
                columns = columns[:-2]
                values = values[:-2]
                if "id" not in columns:
                    columns = "id, " + columns
                    values = str(self.get_next_free_index()) + ", " + values
                self.database.insert(self.db_table, columns, values)
            else:
                print(f"Couldn't save any document data. No valid data.")

    def update_document(self, index, data):
        try:
            if not isinstance(data, dict):
                raise Exception
        except Exception as e:
            print(f"Input data is not valid. Should be a dict:\n{e}")
        else:
            setter = ""
            for key, val in data.items():
                if key in self.db_cols:
                    setter += key + "="
                    if type(val) == str:
                        setter += "'" + val + "', "
                    else:
                        setter += str(val) + ", "
                else:
                    print(f"'{key}' is not supported by table '{self.db_table}'")
            if len(setter) > 0:
                setter = setter[:-2]
                self.database.update(self.db_table, setter, f"id = {index}")
            else:
                print(f"Couldn't update any document data. No valid data.")

    def delete_document(self, index):
        self.database.delete(self.db_table, f"id = {index}")

    def delete_all_documents(self):
        self.database.delete(self.db_table)

    # returns one value
    #
    #

    def get_code_of_document(self, doc_id):
        return self.database.select(self.db_table, "code", f"id = {doc_id}")[0][0]

    # returns one document
    #
    #

    def get_document_by_id(self, index):
        return self.database.select(self.db_table, "*", f"id = {index}")[0]

    def get_print_doc_by_code(self, columns, code):
        data = self.database.select(self.db_table, columns, f"code = '{code}' AND type = 'print'")[0]
        if len(data) > 0:
            return data
        return None

    def get_scan_doc_by_code(self, columns, code):
        data = self.database.select(self.db_table, columns, f"code = '{code}' AND type = 'scan'")[0]
        if len(data) > 0:
            return data
        return None

    # returns multiple documents
    #
    #

    def get_documents_by_path(self, path):
        return self.database.select(self.db_table, "*", f"path = '{path}'")

    def get_documents_by_set_id(self, set_id, columns):
        return self.database.select(self.db_table, columns, f"set_id = {set_id}")

    def get_all_documents(self, columns=None, where=None):
        if where == None:
            if columns == None:
                return self.database.select(self.db_table, "*")
            else:
                return self.database.select(self.db_table, columns)
        else: 
            if columns == None:
                return self.database.select(self.db_table, "*", where)
            else:
                return self.database.select(self.db_table, columns, where)

    # next free ids
    #
    #

    def get_next_free_index(self):
        result = self.database.select_max(self.db_table, "id")
        if result[0] != None:
            return int(result[0]) + 1
        return 0

    def get_next_free_link_id(self, set_id):
        result = self.database.select_max(
            self.db_table, "link_id", f"set_id = {set_id}")
        if result[0] != None:
            return int(result[0]) + 1
        return 0

    def get_next_free_set_id(self):
        result = self.database.select_max(self.db_table, "set_id")
        if result[0] != None:
            return int(result[0]) + 1
        return 0

    # document copy
    #
    #

    def save_doc_copy(self, index, source_path):
        file_name = "doc" + str(index)
        try:
            copyfile(source_path, self.data_path + self.doc_dir + file_name)
        except Exception as e:
            print(f"Could not save a copy of the document. Error: {e}")
        else:
            file_path = os.path.abspath(
                self.data_path + self.doc_dir + file_name)
            self.database.update(self.db_table,
                                 f"data_name = '{file_path}'",
                                 f"id = {index}")

    def delete_doc_copy(self, index):
        file_name = self.database.select(
            self.db_table, "data_name", f"id = {index}")[0][0]
        try:
            os.remove(file_name)
        except Exception as e:
            print(f"Could not delete document copy. Error: {e}")
        else:
            self.database.update(
                self.db_table, "data_name = NULL", f"id = {index}")
