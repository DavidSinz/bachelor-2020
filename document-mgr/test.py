# from db_table import DBTable

# import time


# self.document.create_table("""id                        INT                 PRIMARY KEY,
#                              code                      INT,
#                              title                     VARCHAR(50),
#                              file_name                 VARCHAR(50)         NOT NULL,
#                              path                      VARCHAR(255),
#                              insert_date               DATETIME            NOT NULL,
#                              creation_date             DATETIME,
#                              date_of_update            DATETIME,
#                              date_of_access            DATETIME,
#                              file_type                 VARCHAR(10),
#                              size                      INT,
#                              attribute                 VARCHAR(255),
#                              options                   VARCHAR(255)""")

# if code is None:
#    code = 'NULL'
# self.document.insert_into("""id, code, title, file_name, path, insert_date, creation_date, date_of_update,
#                          date_of_access, file_type, size, attribute, options""",
#                          f"""{index + 1}, {code}, '{title}', '{file_name}', '{path}',
#                          '{time.strftime('%Y-%m-%d %H:%M:%S')}', '{creation_date}', '{date_of_update}',
#                          '{date_of_access}', '{file_type}', {size}, '{attribute}', '{options}'""")

# import time
# from database import Database
# from document import ScanDocument
#
# d = Database('document_mgr')
# s = ScanDocument(123, 'testname', '/test/path', time.strftime('%Y-%m-%d %H:%M:%S'))




