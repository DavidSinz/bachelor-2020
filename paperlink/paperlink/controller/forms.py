from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

class UpdateDocForm(Form):
    context = StringField('Context')
    file_name = StringField('File Name')
    path = StringField('Path')
    size = IntegerField('Size')