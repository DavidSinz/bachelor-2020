import sqlite3


class Database:

    ##########################################################################
    #
    # Class Database
    #
    # This class connects to a database and executes database operations.
    #

    ##########################################################################
    #
    # '__init__'
    #
    # This constructor connects to a database with a given 'database_engine'
    # and a given 'database_file'. It also calls the 'create_table' method
    # which creates new database tables.
    #

    def __init__(self, database_file, table_data):
        self.conn = sqlite3.connect(database_file)
        self.curs = self.conn.cursor()
        self.create_table(table_data)

    ##########################################################################
    #
    # '__del__'
    #
    # This destructor disconnects from the database, if this instance gets
    # deleted.
    #

    def __del__(self):
        self.conn.close()

    ##########################################################################
    #
    # 'create_table'
    #
    # This method creates tables with the 'data' parameter.
    # The 'data' parameter is a dictionary, where the keys table names
    # represent and the values are arrays which store the columns to create.
    # The format of the 'data' dictionary has a format like the following
    # example:
    # data = {
    #   "table1": ["column1", "column2", "column3"],
    #   "table2": ["column4", "column5", "column6"]
    # }
    #

    def create_table(self, data):
        for table_name, table_columns in data.items():
            table_columns = ", ".join(table_columns)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table_columns});"
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
    # data = {
    #   "table1": {"col1": "val1", "col2": "val2", "col3": "val3"},
    #   "table2": {"col4": "val4", "col5": "val5", "col6": "val6"}
    # }
    #

    def insert(self, data):
        for table_name, table_data in data.items():
            columns = ", ".join(list(table_data.keys()))
            values = ", ".join(list(table_data.values()))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            self.curs.execute(query)
        self.conn.commit()

    ##########################################################################
    #
    # 'select'
    #
    # This method selects entries from a database table. The
    # parameter 'data' has the following format:
    # data = {
    #   "table1": {"column": ["*"], "where": "col1 = val1"},
    #   "table2": {"column": ["col1", "col2"]}
    # }
    # - table1 selects all columns where col1 is val1
    # - table2 selects only col1 and col2 without a where condition
    #

    def select(self, data):
        result_data = []
        for table_name, table_data in data.items():
            columns = ", ".join(table_data["column"])
            query = f"SELECT {columns} FROM {table_name}"
            if table_data.get("where") is not None:
                where = table_data["where"]
                query += f" WHERE {where};"
            else: query += ";"
            self.curs.execute(query)
            result_data += self.curs.fetchall()
        return result_data

    ##########################################################################
    #
    # 'update'
    #
    # This method updates entries of a database table. The
    # parameter 'data' has the following format:
    # data = {
    #   "table1": {
    #     "set": {"col1": "val1", "col2": "val2", "col3": "val3"},
    #     "where": "col1 = val10"
    #   },
    #   "table2": {
    #     "set": {"col4": "val4", "col5": "val5", "col6": "val6"}
    #   }
    # }
    # - table1 updates col1 to col3 with val1 to val3 where the value of col1
    #   is val10
    # - table2 updates col4 to col6 with val4 to val6 without a where
    #   condition
    #

    def update(self, data):
        for table_name, table_data in data.items():
            setter = ""
            for column, value in table_data.get("set").items():
                setter += column + " = " + value + ", "
            setter = setter[:-2]
            query = f"UPDATE {table_name} SET {setter}"
            if table_data.get("where") is not None:
                where = table_data.get("where")
                query += f" WHERE {where};"
            else: query += ";"
            self.curs.execute(query)
        self.conn.commit()

    ##########################################################################
    #
    # 'delete'
    #
    # This method deletes entries from a database table. The
    # parameter 'data' has the following format:
    # data = {
    #   "table1": {},
    #   "table2": {"where": "col1 = val1"}
    # }
    # - table1 will be entirely deleted
    # - An entry with the val1 for col1 is deleted from table2
    #

    def delete(self, data):
        for table_name, table_data in data.items():
            query = f"DELETE FROM {table_name}"
            if table_data.get("where") is not None:
                where = table_data.get("where")
                query += f" WHERE {where};"
            else: query += ";"
            self.curs.execute(query)
        self.conn.commit()
