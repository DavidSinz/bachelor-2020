# import modules
import sqlite3
import time

# import custom
from db_table import DatabaseTable as Table


class Database:

    # create connection to database
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'db/{db_name}.db')
        self.curs = self.conn.cursor()

        # create database table instance
        self.document = Table(self.conn, self.curs, 'document')
        self.create_table_document()

    # init table document
    def create_table_document(self):
        self.document.create_table("""id                        INT                 PRIMARY KEY,
                                      code                      INT,
                                      title                     VARCHAR(50)
                                      file_name                 VARCHAR(50)         NOT NULL,
                                      path                      VARCHAR(255),
                                      insert_date               DATETIME            NOT NULL,
                                      creation_date             DATETIME,
                                      date_of_update            DATETIME,
                                      date_of_access            DATETIME,
                                      file_type                 VARCHAR(10),
                                      size                      INT,
                                      attribute                 VARCHAR(255),
                                      options                   VARCHAR(255)""")

    def insert_document(self, file_name, code=None, title=None, path=None, creation_date=None, date_of_update=None,
                        date_of_access=None, file_type=None, size=None, attribute=None, options=None):
        index = self.document.max_of_column("id")
        if index is None:
            index = 0
        self.document.insert_into("""id, code, title, file_name, path, insert_date, creation_date, date_of_update, 
                                  date_of_access, file_type, size, attribute, options""",
                                  f"""{index + 1}, {code}, '{title}', '{file_name}', '{path}', 
                                  '{time.strftime('%Y-%m-%d %H:%M:%S')}', '{creation_date}', '{date_of_update}', 
                                  '{date_of_access}', '{file_type}', {size}, '{attribute}', '{options}'""")

    def select_all_document(self):
        return self.document.select_all()

    # close database
    def __del__(self):
        self.conn.close()
