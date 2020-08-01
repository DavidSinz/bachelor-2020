class Database:
    ##########################################################################
    #
    # Class Database
    #
    # This class initializes a database and creates tables for it, if they
    # are not already existing.
    #
    # '__init__': This constructor connects to a database with a given
    # 'database_engine' and a given 'database_file'
    #
    # 'create_table': This method creates a table with the 'data' parameter.
    # The 'data' parameter is a dictionary and the key is the 'table_name'
    # and the value is an array which stores the columns to create
    #

    def __init__(self, database_engine, database_file):
        self.conn = database_engine.connect(database_file)
        self.curs = self.conn.cursor()

    def create_table(self, data):
        table_name = list(data.keys())[0]
        table_columns = ','.join(data[table_name])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table_columns});"
        self.conn.execute(query)
        self.conn.commit()

    # find the max id
    def max_of_column(self, column):
        query = f"SELECT max({column}) FROM {self.name};"
        self.curs.execute(query)
        data = self.curs.fetchone()
        return data[0]

    # find the next available unique id for a new table row
    @staticmethod
    def determine_unique_id(table):
        index = table.max_of_column("id")
        if index is None:
            index = -1
        return index + 1



    # display data of choice
    def select_from(self, where):
        query = f"SELECT * FROM {self.name} WHERE {where};"
        self.curs.execute(query)
        return self.curs.fetchall()

    # display all data
    def select_all(self):
        query = f"SELECT * FROM {self.name};"
        self.curs.execute(query)
        return self.curs.fetchall()

    # insert into table
    def insert_into(self, columns, values):
        query = f"INSERT INTO {self.name} ({columns}) VALUES ({values});"
        self.curs.execute(query)
        self.conn.commit()

    # update table content
    def update(self, setter, where):
        query = f"UPDATE {self.name} SET {setter} WHERE {where};"
        self.curs.execute(query)
        self.conn.commit()

    # delete table content
    def delete(self, where):
        query = f"DELETE FROM {self.name} WHERE {where};"
        self.curs.execute(query)
        self.conn.commit()

    # join two tables
    def select_all_join(self, table, join_col, t_join_col):
        query = f"""SELECT * FROM {self.name} INNER JOIN {table.name} 
                ON {self.name}.{join_col} = {table.name}.{t_join_col};"""
        self.curs.execute(query)
        return self.curs.fetchall()

    # close the connection to the database, if a instance of this class gets
    # deleted
    def __del__(self):
        self.conn.close()
