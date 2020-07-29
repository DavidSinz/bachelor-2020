import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('db/document.db')
        self.create_table()
        self.curs = self.conn.cursor()
    #CreatesTable
    def create_table(self):

        self.conn.execute("""CREATE TABLE IF NOT EXISTS document (
                              id                        STRING           PRIMARY KEY         NOT NULL,
                              code_id                   STRING           NOT NULL,
                              file_name                 STRING           NOT NULL,
                              path                      STRING           NOT NULL,
                              insert_date               STRING           NOT NULL,
                              creation_date             STRING           NOT NULL,
                              date_of_update            STRING           NOT NULL,
                              date_of_last_access       STRING           NOT NULL,
                              file_type                 STRING           NOT NULL,
                              size                      STRING           NOT NULL,   
                              attribute                 STRING           NOT NULL,         
                              optionsTEXT               STRING           NOT NULL)""")
        self.conn.commit()

    #to display data of choice
    def select_from(self, index):
        count_for =  self.curs.execute("SELECT * FROM document")
        length = len(count_for.fetchall())
        self.curs.execute("SELECT * FROM document WHERE QR_code = {}".format(index))
        return self.curs.fetchall()
        self.conn.commit()
    #displays all data
    def select_all(self):
        all_data =self.curs.execute("SELECT * FROM document").fetchall()
        print(all_data)


    #Insert
    def insert_into(self,QR_code,file_name,path,insert_date,creation_date,date_of_update,date_of_last_access,file_type,size,attribute,optionsTEXT):
        #make_id makes the id automaticallyy whenever new data is stored
        count = self.curs.execute("SELECT * FROM document").fetchall()
        length = len(count)
        make_id = 'Q0'+ str(length+1)
        self.curs.execute("Insert into document(id,QR_code,file_name,path,insert_date,creation_date,date_of_update,date_of_last_access,file_type,size,attribute,optionsTEXT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                          (make_id,QR_code,file_name,path,insert_date,creation_date,date_of_update,date_of_last_access,file_type,size,attribute,optionsTEXT))

        self.conn.commit()

    #Update

    def update(self, query):

        self.curs.execute(query)
        self.conn.commit()

    #Delete

    def delete(self,id):
        self.curs.execute("DELETE FROM document WHERE id = {}".format(id))

        self.conn.commit()

    #Closing DB

    def __del__(self):
        self.conn.close()

