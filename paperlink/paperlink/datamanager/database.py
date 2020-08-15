import sqlite3


class Database:
    """Class to enable database interactions.

    This class connects to a database and executes database operations.
    It is able to execute the following basic queries: create table, insert
    select, update and delete. It also can select from two joined tables. By 
    creating instances of this class, there will be created a database file 
    if not already existing. Therefor it's possible to connect to different 
    databases with different instances and it's also possible to connect to 
    only one database with different instances  of this class. This class uses 
    a SQLite database and therfor imports the sqlite3 python module.

    Attributes:
        conn: A connection to a database.
        curs: A cursor to fetch query results.
    """



    def __init__(self, db_file):
        """Inits Database class and creates a connection to a database and a 
        curser to fetch data output."""
        try:
            self.conn = sqlite3.connect(db_file)
            self.curs = self.conn.cursor()
        except Exception as e:
            print("Error: " + e)



    def __del__(self):
        """Closes this database connection, when this instance is deleted."""
        try:
            self.conn.close()
        except Exception as e:
            print("Error: " + e)



    def create_table(self, table_name, columns):
        """Executes a SQL CREATE TABLE IF NOT EXISTS statement.

        The CREATE TABLE IF NOT EXISTS statement is used to create a table in 
        a database, if that table has not already been created.

        Example query: 
            CREATE TABLE IF NOT EXISTS table_name (column1, column2, ...);

        Typical use:
            table_name = "table"
            columns = "col1, col2"
            d = Database(...)
            d.create_table(table_name, columns)

        The example shown above will create a table, if that table has not 
        already been created and defines the columns col1 and col2 for that 
        table.
        """
        self._commit(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")



    def insert(self, table_name, columns, values):
        """Executes a SQL INSERT INTO Statement.

        The INSERT INTO statement is used to insert new records in a table.

        Example query: 
            INSERT INTO table_name (column1, column2, ...)
            VALUES (value1, value2, ...); 

        Typical use:
            table_name = "table"
            columns = "col1, col2"
            values = "val1, val2"
            d = Database(...)
            d.insert(table_name, columns, values)

        The example shown above will insert a record into an table and sets a 
        column named col1 to a value named val1 and so on. 
        """
        self._commit(f"""INSERT INTO {table_name} 
            ({columns}) VALUES ({values});""")



    def select(self, table_name, columns, condition=None):
        """Executes a SQL SELECT Statement.

        The SELECT statement is used to select data from a database.

        Example query:
            SELECT column1, column2, ... FROM table_name WHERE condition;

        Typical use:
            table_name = "table"
            columns = "col1, col2"
            condition = "col3 = val3"
            d = Database(...)
            d.select(table_name, columns, condition)

        The example shown above will select records of an table where a column 
        called col3 equals a value named val3. The result values are related 
        to the columns col1 and col2. 
        
        The optional condition argument can be omitted, which will select all  
        entries of a table.
        """
        query = f"SELECT {columns} FROM {table_name};"
        if condition is not None:
            query = query[:-1] + f" WHERE {condition};"
        return self._fetch_all(query)



    def joined_select(self, table1, table2, join1, join2, columns, condition=None):
        """Executes a SQL INNER JOIN Statement.

        The INNER JOIN keyword selects records that have matching values in 
        both tables.

        Example query:
            SELECT columns
            FROM table1
            INNER JOIN table2
            ON table1.join1 = table2.join2
            WHERE condition;

        Typical use:
            table_name1 = "table1"
            table_name2 = "table2"
            join_col1 = "join1"
            join_col2 = "join2"
            columns = "col1, col2"
            condition = "col3 = val3"
            d = Database(...)
            d.select(table_name1, table_name2, join_col1, 
                     join_col2, columns, condition)

        The example shown above will select records of two joined tables, 
        where a column called col3 equals a value named val3. The result 
        values are related to the columns col1 and col2. 
        
        The optional condition argument can be omitted, which will select all  
        entries of two joined tables, in respect to the inner join selection.
        """
        query = f"""SELECT {columns} FROM {table1} 
                INNER JOIN {table2} ON {table1}.{join1} = {table2}.{join2};"""
        if condition is not None:
            query = query[:-1] + f" WHERE {condition};"
        return self._fetch_all(query)



    def select_max(self, table_name, column, condition=None):
        """Executes a SQL SELECT Statement to select a maximum.

        The SELECT statement is used to select data from a database. Combined 
        with the max function, it selects a entry with the maximum value of a 
        column.

        Example query:
            SELECT MAX(column1) FROM table_name WHERE condition;

        Typical use:
            table_name = "table"
            column = "col1"
            condition = "col2 = val2"
            d = Database(...)
            d.select(table_name, column, condition)

        The example shown above will select the record with the highest value 
        of an column named col1, where a column called col2 equals a value 
        named val2. 
        
        The optional condition argument can be omitted, which will select all  
        entries of a table and gets the maximum of them.
        """
        query = f"SELECT MAX({column}) FROM {table_name};"
        if condition is not None:
            query = query[:-1] + f" WHERE {condition};"
        return self._fetch_one(query)



    def update(self, table_name, set_arg, condition=None):
        """Executes a SQL UPDATE statement.

        The UPDATE statement is used to modify the existing records in a table.

        Example query: 
            UPDATE table_name 
            SET column1 = value1, column2 = value2, ...
            WHERE condition;

        Typical use:
            table_name = "table"
            set_arg = "col1 = val1, col2 = val2"
            condition = "col3 = val3"
            d = Database(...)
            d.update(table_name, set_arg, condition)

        The example shown above will update a record of an table where the 
        column named col3 has the value val3 and sets the values of the 
        columns col1 and col2 to the values val1 and val2.
        
        The optional condition argument can be omitted, which will update 
        all entries of a table.
        """
        query = f"UPDATE {table_name} SET {set_arg};"
        if condition is not None:
            query = query[:-1] + f" WHERE {condition};"
        self._commit(query)



    def delete(self, table_name, condition=None):
        """Executes a SQL DELETE statement.

        The DELETE statement is used to delete existing records in a table.

        Example query: 
            DELETE FROM table_name WHERE condition;

        Typical use:
            table_name = "table"
            condition = "col = val"
            d = Database(...)
            d.delete(table_name, condition)

        The example shown above will delete a record where the column named 
        col equals the value named val.

        The optional condition argument can be omitted, which will delete 
        all entries of a table.
        """
        query = f"DELETE FROM {table_name};"
        if condition is not None:
            query = query[:-1] + f" WHERE {condition};"
        self._commit(query)



    def _commit(self, query):
        """Commits a query to a table as data input."""
        try:
            self.conn.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error: " + e)



    def _fetch_all(self, query):
        """Fetches query results as data output."""
        try:
            self.curs.execute(query)
            return self.curs.fetchall()
        except Exception as e:
            print("Error: " + e)
            return None



    def _fetch_one(self, query):
        """Fetches one result of a query as data output."""
        try:
            self.curs.execute(query)
            return self.curs.fetchone()
        except Exception as e:
            print("Error: " + e)
            return None
