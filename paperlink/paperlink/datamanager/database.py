import sqlite3


class Database:

    """class 'database'
    
    This class connects to a database and executes database operations.
    It is able to execute the following basic queries: create table, insert
    select, update and delete. By creating instances of this class, there
    will be created a database file if not already existing. Therefor it's
    possible to connect to different databases with different instances and
    it's also possible to connect to only one database with different
    instances  of this class.

    - database engine: sqlite3
    
    """

    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    """Helper to print a traceback from the timed code.

    Typical use:

        t = Timer(...)       # outside the try/except
        try:
            t.timeit(...)    # or t.repeat(...)
        except:
            t.print_exc()

    The advantage over the standard traceback is that source lines
    in the compiled template will be displayed.

    The optional file argument directs where the traceback is
    sent; it defaults to sys.stderr.
    """

    def __init__(self, db_file):
        """Inits SampleClass with blah."""
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            print(f"\nCould not connect to {db_file} database:\n{e}\n")
        else:
            self._init_cursor()

    def _init_cursor(self):
        try:
            self.curs = self.conn.cursor()
        except Exception as e:
            print(f"\nCould not create database cursor:\n{e}\n")

    def _commit(self, query):
        try:
            self.conn.execute(query)
            self.conn.commit()
        except Exception as e:
            print(f"""\nCouldn't commit query to database:
                \n{query}\nError:\n{e}\n""")

    def _fetch_all(self, query):
        try:
            self.curs.execute(query)
            return self.curs.fetchall()
        except Exception as e:
            print(f"""\nCouldn't fetch query result from database:
                \n{query}\nError:\n{e}\n""")
            return None

    def _fetch_one(self, query):
        try:
            self.curs.execute(query)
            return self.curs.fetchone()
        except Exception as e:
            print(f"""\nCouldn't fetch query result from database:
                \n{query}\nError:\n{e}\n""")
            return None

    def __del__(self):
        try:
            self.conn.close()
        except Exception as e:
            print(f"\nThe database connection can't be closed:\n{e}\n")

    # ==========================================================================
    #
    # method 'create_table'
    #
    # This method creates tables with the 'data' parameter. 'data' saves a
    # dictionary, where the keys table names represent and the values
    # represent the column names. The 'data' dictionary has a format like the
    # following example:
    #

    def create_table(self, table_name, columns):
        self._commit(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")

    # ==========================================================================
    #
    # method 'insert'
    #
    # This method inserts data into database tables. The parameter
    # 'data' has the following format:
    #

    def insert(self, table_name, columns, values):
        self._commit(f"""INSERT INTO {table_name} 
            ({columns}) VALUES ({values});""")

    # ==========================================================================
    #
    # method 'select'
    #
    # This method selects entries from a database table. The
    # parameter 'data' has the following format:
    #

    def select(self, table_name, columns, where=None, group_by=None, order_by=None):
        query = f"SELECT {columns} FROM {table_name};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        if group_by is not None:
            query = query[:-1] + f" GROUP BY {group_by};"
        if order_by is not None:
            query = query[:-1] + f" ORDER BY {order_by};"
        return self._fetch_all(query)

    def joined_select(self, table1, table2, join1, join2, columns, where=None):
        query = f"""SELECT {columns} FROM {table1} 
                INNER JOIN {table2} ON {table1}.{join1} = {table2}.{join2};"""
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        return self._fetch_all(query)

    def select_max(self, table_name, column, where=None):
        if where != None:
            query = f"SELECT max({column}) FROM {table_name} WHERE {where};"
        else:
            query = f"SELECT max({column}) FROM {table_name};"
        return self._fetch_one(query)

    # ==========================================================================
    #
    # method 'update'
    #
    # This method updates entries of a database table. The
    # parameter 'data' has the following format:
    #

    def update(self, table_name, setter, where=None):
        query = f"UPDATE {table_name} SET {setter};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        self._commit(query)

    # ==========================================================================
    #
    # method 'delete'
    #
    # This method deletes entries from a database table. The
    # parameter 'data' has the following format:
    #

    def delete(self, table_name, where=None):
        query = f"DELETE FROM {table_name};"
        if where is not None:
            query = query[:-1] + f" WHERE {where};"
        self._commit(query)
