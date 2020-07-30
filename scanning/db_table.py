# import custom
from database import Database


class DBTable(Database):

    # init DBTable
    def __init__(self, db_name, table_name):
        super().__init__(db_name)
        self.table_name = table_name

    # create a table if it's not already existing
    def create_table(self, data):
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({data})")
        self.conn.commit()

    # find the max id
    def max_of_column(self, column):
        self.curs.execute(f"SELECT max({column}) FROM {self.table_name}")
        data = self.curs.fetchone()
        if data is None:
            return -1
        print(data[0])

    # display data of choice
    def select_from(self, where):
        self.curs.execute(f"SELECT * FROM {self.table_name} WHERE {where}")
        print(self.curs.fetchall())

    # display all data
    def select_all(self):
        self.curs.execute(f"SELECT * FROM {self.table_name}")
        print(self.curs.fetchall())

    # insert into table
    def insert_into(self, columns, values):
        self.curs.execute(f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    # update table content
    def update(self, setter, where):
        self.curs.execute(f"UPDATE {self.table_name} SET {setter} WHERE {where}")
        self.conn.commit()

    # delete table content
    def delete(self, where):
        self.curs.execute(f"DELETE FROM {self.table_name} WHERE {where}")
        self.conn.commit()
