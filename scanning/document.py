class Document:

    # init document
    def __init__(self, name, path, title, f_type, code):
        self.name = name
        self.path = path
        self.title = title
        self.f_type = f_type
        self.code = code

    # set path
    def set_path(self, path):
        self.path = path

    # return path
    def get_path(self):
        return self.path
