# import modules
import sqlite3

# custom modules
import output


class DatabaseTable:

    # init database table
    def __init__(self, connection, cursor, table_name):
        self.conn = connection
        self.curs = cursor
        self.name = table_name

    # create a table if it's not already existing
    def create_table(self, data):
        query = f"CREATE TABLE IF NOT EXISTS {self.name} ({data});"
        output.debug(query)
        self.conn.execute(query)
        self.conn.commit()

    # find the max id
    def max_of_column(self, column):
        query = f"SELECT max({column}) FROM {self.name};"
        output.debug(query)
        self.curs.execute(query)
        data = self.curs.fetchone()
        return data[0]

    # display data of choice
    def select_from(self, where):
        query = f"SELECT * FROM {self.name} WHERE {where};"
        output.debug(query)
        self.curs.execute(query)
        return self.curs.fetchall()

    # display all data
    def select_all(self):
        query = f"SELECT * FROM {self.name};"
        output.debug(query)
        self.curs.execute(query)
        return self.curs.fetchall()

    # insert into table
    def insert_into(self, columns, values):
        query = f"INSERT INTO {self.name} ({columns}) VALUES ({values});"
        output.debug(query)
        self.curs.execute(query)
        self.conn.commit()

    # update table content
    def update(self, setter, where):
        query = f"UPDATE {self.name} SET {setter} WHERE {where};"
        output.debug(query)
        self.curs.execute(query)
        self.conn.commit()

    # delete table content
    def delete(self, where):
        query = f"DELETE FROM {self.name} WHERE {where};"
        output.debug(query)
        self.curs.execute(query)
        self.conn.commit()

    # join two tables
    def select_all_join(self, table, join_col, t_join_col):
        query = f"""SELECT * FROM {self.name} INNER JOIN {table.name} 
                ON {self.name}.{join_col} = {table.name}.{t_join_col};"""
        output.debug(query)
        self.curs.execute(query)
        output.debug(list(map(lambda x: x[0], self.curs.description)))
        return self.curs.fetchall()


class Database:

    # create connection to database
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'db/{db_name}.db')
        self.curs = self.conn.cursor()

        # create instances of class DatabaseTable
        self.document = DatabaseTable(self.conn, self.curs, 'document')
        self.digital_doc = DatabaseTable(self.conn, self.curs, 'digital_document')
        self.scan_doc = DatabaseTable(self.conn, self.curs, 'scan_document')
        self.create_tables()

    # create tables
    def create_tables(self):
        self.document.create_table(
            "id INT PRIMARY KEY, code INT, file_name VARCHAR(50), path VARCHAR(50), insert_date DATETIME")
        self.digital_doc.create_table("id INT PRIMARY KEY, document_id INT")
        self.scan_doc.create_table("id INT PRIMARY KEY, document_id INT")

    # find the next available unique id for a new table row
    @staticmethod
    def determine_unique_id(table):
        index = table.max_of_column("id")
        if index is None:
            index = -1
        return index + 1

    # insert into scan_document and document table
    def insert_scan_doc(self, *args):
        doc_id = self.determine_unique_id(self.document)
        scan_id = self.determine_unique_id(self.scan_doc)
        self.document.insert_into("id, code, file_name, path", f"{doc_id}, {args[0]}, '{args[1]}', '{args[2]}'")
        self.scan_doc.insert_into("id, document_id", f"{scan_id}, {doc_id}")

    # join two tables and select al columns
    def select_all_scan_doc(self):
        return self.scan_doc.select_all_join(self.document, 'document_id', 'id')

    # close database
    def __del__(self):
        self.conn.close()
