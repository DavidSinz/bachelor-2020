class DatabaseTable:

    # init database table
    def __init__(self, connection, cursor, table_name):
        self.conn = connection
        self.curs = cursor
        self.name = table_name

    # create a table if it's not already existing
    def create_table(self, data):
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({data})")
        self.conn.commit()

    # find the max id
    def max_of_column(self, column):
        self.curs.execute(f"SELECT max({column}) FROM {self.name}")
        data = self.curs.fetchone()
        return data[0]

    # display data of choice
    def select_from(self, where):
        self.curs.execute(f"SELECT * FROM {self.name} WHERE {where}")
        return self.curs.fetchall()

    # display all data
    def select_all(self):
        self.curs.execute(f"SELECT * FROM {self.name}")
        return self.curs.fetchall()

    # insert into table
    def insert_into(self, columns, values):
        self.curs.execute(f"INSERT INTO {self.name} ({columns}) VALUES ({values})")
        self.conn.commit()

    # update table content
    def update(self, setter, where):
        self.curs.execute(f"UPDATE {self.name} SET {setter} WHERE {where}")
        self.conn.commit()

    # delete table content
    def delete(self, where):
        self.curs.execute(f"DELETE FROM {self.name} WHERE {where}")
        self.conn.commit()
