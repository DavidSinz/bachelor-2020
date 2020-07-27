import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('db/document.db')
        self.create_table()
        self.curs = self.conn.cursor()

    def create_table(self):
        try:
            self.conn.execute("""CREATE TABLE document (
                              id             INT             PRIMARY KEY         NOT NULL,
                              title          TEXT            NOT NULL,
                              name           TEXT            NOT NULL,
                              path           TEXT            NOT NULL,
                              time           TEXT            NOT NULL)""")
            self.conn.commit()
            print('Table was successfully created')
        except sqlite3.OperationalError:
            print('Table was already created')

    def select_from(self, index):
        self.curs.execute("SELECT * FROM document WHERE id = {}".format(index))
        print(self.curs.fetchall())
        self.conn.commit()

    def insert_into(self):
        self.curs.execute("INSERT INTO document (id, title, name, path, time) \
              VALUES (0, 'test', 'test name', '/path/test/doc.pdf', '2020-07-15 15:10:03.123')")
        self.conn.commit()

    def update(self, index):
        self.curs.execute("UPDATE document SET path = '/other/path/doc.pdf' WHERE id = {}".format(index))
        self.conn.commit()

    def delete(self, index):
        self.curs.execute("DELETE FROM document WHERE id = {}".format(index))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
