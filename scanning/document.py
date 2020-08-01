# custom modules
import output


class Document:

    def __init__(self, code, file_name, path, insert_date):
        self.code = code
        self.file_name = file_name
        self.path = path
        self.insert_date = insert_date

    def get_code(self):
        return self.code

    def get_file_name(self):
        return self.file_name

    def get_path(self):
        return self.path

    def get_insert_date(self):
        return self.insert_date


class DigitalDocument(Document):

    def create(self, code, file_name, path, insert_date):
        super().__init__(code, file_name, path, insert_date)


class ScanDocument(Document):

    def create(self, code, file_name, path, insert_date):
        super().__init__(code, file_name, path, insert_date)


class DocumentHistory:

    def __init__(self):
        pass
