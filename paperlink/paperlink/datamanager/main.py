"""DataManager

This is the DataManager. Here will be all the files be stored and accessable
for using purposes
"""

import os
import sys
import ast
import getopt

from datamanager.database import Database

# Database information
db_path = "datamanager/db/"
db_name = "document.db"
db_table = "document"
db_create = """id           INT             PRIMARY KEY, 
            name            VARCHAR(255)    NOT NULL, 
            path            VARCHAR(4096), 
            code            VARCHAR(255)    NOT NULL, 
            linking         VARCHAR(255)    NOT NULL, 
            file_type       VARCHAR(8), 
            size            INT, 
            type            VARCHAR(8)      NOT NULL, 
            insert_date     DATETIME        NOT NULL, 
            dumped          INT             NOT NULL, 
            data_name       VARCHAR(255), 
            screenshot      VARCHAR(255)"""
db_cols = """id, name, path, code, linking, file_type, size, type, 
          insert_date, dumped, data_name, screenshot"""

# Data directory information
doc_dir = "data/doc/"
img_dir = "data/img/"

# Objects
database = Database(db_path + db_name)


def save_document(data):
    try:
        data = ast.literal_eval(data)
    except Exception as e:
        print(f"Input data '{data}' is not valid. Should be a dict:\n{e}")
    else:
        columns = ""
        values = ""
        for key, val in data.items():
            if key in db_cols:
                columns += key + ", "
                if type(val) == str:
                    values += "'" + val + "', "
                else:
                    values += str(val) + ", "
            else:
                print(f"'{key}' is not supported by table '{db_table}'")
        if len(columns) > 0:
            columns = columns[:-2]
            values = values[:-2]
            if "id" not in columns:
                columns = "id, " + columns
                values = str(_get_next_free_index()) + ", " + values
            database.insert(db_table, columns, values)
        else:
            print(f"Couldn't save any document data. No valid data.")


def update_document(index, data):
    try:
        data = ast.literal_eval(data)
    except Exception as e:
        print(f"Input data '{data}' is not valid. Should be a dict:\n{e}")
    else:
        setter = ""
        for key, val in data.items():
            if key in db_cols:
                setter += key + "="
                if type(val) == str:
                    setter += "'" + val + "', "
                else:
                    setter += str(val) + ", "
            else:
                print(f"'{key}' is not supported by table '{db_table}'")
        if len(setter) > 0:
            setter = setter[:-2]
            database.update(db_table, setter, f"id = {index}")
        else:
            print(f"Couldn't update any document data. No valid data.")


def delete_document(index):
    database.delete(db_table, f"id = {index}")


def delete_all_documents():
    database.delete(db_table)


def get_document(index):
    return database.select(db_table, "*", f"id = {index}")


def get_all_documents():
    return database.select(db_table, "*")


def _get_next_free_index():
    result = database.select_max(db_table, "id")
    if result[0] != None:
        print(result)
        return int(result[0]) + 1
    return 0


def save_screenshot(index, image_data):
    file_name = "screenshot" + str(index) + ".png"
    try:
        with open(img_dir + file_name, 'w') as file:
            file.write(image_data)
    except Exception as e:
        print(f"Could not save the screenshot. Error: {e}")
    else:
        file_path = os.path.abspath(img_dir + file_name)
        database.update(db_table,
                        f"screenshot = '{file_path}'",
                        f"id = {index}")


def delete_screenshot(index):
    file_name = database.select(db_table, "screenshot", f"id = {index}")[0][0]
    try:
        os.remove(file_name)
    except Exception as e:
        print(f"Could not delete screenshot. Error: {e}")
    else:
        database.update(db_table, "screenshot = NULL", f"id = {index}")


def save_doc_copy(index, document_data):
    file_name = "doc" + str(index)
    try:
        with open(doc_dir + file_name, 'w') as file:
            file.write(document_data)
    except Exception as e:
        print(f"Could not save a copy of the document. Error: {e}")
    else:
        file_path = os.path.abspath(doc_dir + file_name)
        database.update(db_table,
                        f"data_name = '{file_path}'",
                        f"id = {index}")


def delete_doc_copy(index):
    file_name = database.select(db_table, "data_name", f"id = {index}")[0][0]
    try:
        os.remove(file_name)
    except Exception as e:
        print(f"Could not delete document copy. Error: {e}")
    else:
        database.update(db_table, "data_name = NULL", f"id = {index}")


def _operation(argv):
    result = None
    index = None
    value = None
    saving = False
    update = False
    delete = False
    get = False
    save_scr = None
    delete_scr = None
    save_copy = None
    delete_copy = None

    try:
        opts, args = getopt.getopt(argv, "hsudgi:v:",
                                   ["screenshot=", "doccopy=",
                                    "deletescreenshot=",
                                    "deletedoccopy="])
    except getopt.GetoptError:
        print("wrong option")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("help")
            sys.exit()
        elif opt == "-s":
            saving = True
        elif opt == "-u":
            update = True
        elif opt == "-d":
            delete = True
        elif opt == "-g":
            get = True
        elif opt == "-i":
            index = arg
        elif opt == "-v":
            value = arg
        elif opt == "--screenshot":
            save_scr = arg
        elif opt == "--doccopy":
            save_copy = arg
        elif opt == "--deletescreenshot":
            delete_scr = arg
        elif opt == "--deletedoccopy":
            delete_copy = arg

    if saving and value != None and not (update or delete or get):
        save_document(value)
    elif update and value != None and index != None and not (saving or delete or get):
        update_document(index, value)
    elif delete and index != None and not (saving or update or get):
        delete_document(index)
    elif delete and index == None and not (saving or update or get):
        delete_all_documents()
    elif get and index != None and not (saving or update or delete):
        print(index)
        result = get_document(index)
    elif get and index == None and not (saving or update or delete):
        result = get_all_documents()
    elif save_scr != None and index != None:
        save_screenshot(index, save_scr)
    elif save_copy != None and index != None:
        save_doc_copy(index, save_copy)
    elif delete_scr != None:
        delete_screenshot(delete_scr)
    elif delete_copy != None:
        delete_doc_copy(delete_copy)

    return result


def main(argv):
    database.create_table(db_table, db_cols)
    result = _operation(argv)
    if result != None:
        print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
