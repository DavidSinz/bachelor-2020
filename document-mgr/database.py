import sqlite3


class Database:

    ##########################################################################
    #
    # Class Database
    #
    # This class connects to a database and executes database operations.
    # It is able to execute the following basic queries: create table, insert
    # select, update and delete. By creating instances of this class, there
    # will be created a database file if not already existing. Therefor it's
    # possible to connect to different databases with different instances and
    # it's also possible to connect to only one database with different
    # instances  of this class.
    #
    # - database engine: sqlite3
    #

    ##########################################################################
    #
    # '__init__'
    #
    # This constructor connects to a sqlite3 database which is stored in a
    # 'database_file'.
    #

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.curs = self.conn.cursor()

    ##########################################################################
    #
    # '__del__'
    #
    # This destructor disconnects from the database, if an instance gets
    # deleted.
    #

    def __del__(self):
        self.conn.close()

    ##########################################################################
    #
    # 'create_table'
    #
    # This method creates tables with the 'data' parameter. 'data' saves a
    # dictionary, where the keys table names represent and the values
    # represent the column names. The 'data' dictionary has a format like the
    # following example:
    #

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        self.conn.execute(query)
        self.conn.commit()

    ##########################################################################
    #
    # Class methods to interact with the database
    #
    # The following methods either select, insert, update or delete entries
    # of a given database table.
    #

    ##########################################################################
    #
    # 'insert'
    #
    # This method inserts data into database tables. The parameter
    # 'data' has the following format:
    #

    def insert(self, table_name, columns, values):
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        self.curs.execute(query)
        self.conn.commit()

    ##########################################################################
    #
    # 'select'
    #
    # This method selects entries from a database table. The
    # parameter 'data' has the following format:
    #

    def select(self, table_name, columns, where=None):
        query = f"SELECT {columns} FROM {table_name};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        self.curs.execute(query)
        return self.curs.fetchall()

    def select_max(self, table_name, column):
        query = f"SELECT max({column}) FROM {table_name};"
        self.curs.execute(query)
        return self.curs.fetchone()

    ##########################################################################
    #
    # 'update'
    #
    # This method updates entries of a database table. The
    # parameter 'data' has the following format:
    #

    def update(self, table_name, setter, where=None):
        query = f"UPDATE {table_name} SET {setter};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        self.curs.execute(query)
        self.conn.commit()

    ##########################################################################
    #
    # 'delete'
    #
    # This method deletes entries from a database table. The
    # parameter 'data' has the following format:
    #

    def delete(self, table_name, where=None):
        query = f"DELETE FROM {table_name};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        self.curs.execute(query)
        self.conn.commit()
