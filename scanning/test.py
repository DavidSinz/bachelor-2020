#from db_table import DBTable

#import time

#db = DBTable('test', 'test')

#db.create_table("""id                        INT                 PRIMARY KEY,
#                              code_id                   INT,
#                              file_name                 VARCHAR(50)         NOT NULL,
#                              path                      VARCHAR(255),
#                              insert_date               DATETIME            NOT NULL,
#                              creation_date             DATETIME,
#                              date_of_update            DATETIME,
#                              date_of_last_access       DATETIME,
#                              file_type                 VARCHAR(10),
#                              size                      INT,
#                              attribute                 VARCHAR(255),
#                              options                   VARCHAR(255)""")

# db.insert_into(f"id, file_name, insert_date", f"1, 'hello', '{time.strftime('%Y-%m-%d %H:%M:%S')}'")
# db.select_all()

from log import Log

l = Log
l.display_list([2,3,4,5,76,8,8,3])
