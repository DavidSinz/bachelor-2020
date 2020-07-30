import sqlite3


class Database:

    # create connection to database
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'db/{db_name}.db')
        self.curs = self.conn.cursor()

    # close database
    def __del__(self):
        self.conn.close()
