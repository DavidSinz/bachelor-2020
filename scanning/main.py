#!/usr/bin/python

# import modules
import sys
import getopt
import logging
from PIL import Image
from pyzbar.pyzbar import decode

# import ghostscript


# import custom
import database


def decode_code(file_name):
    data_objects = decode(Image.open(file_name))
    doc_id = -1

    for obj in data_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data)
        doc_id = int(obj.data.decode("utf-8"))

    return doc_id


def register_doc():
    pass


def pdf_to_image():
    # TODO with ghostscript
    pass


def check_file_format(file_name):
    try:
        Image.open(file_name)
        return True
    except Exception as e:
        print(e)
        if file_name.lower().endswith('.pdf'):
            pdf_to_image()


def main(argv):
    input_file = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:', ['i_file='])
    except getopt.GetoptError:
        print('usage: main.py -i <input_file>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('usage: main.py -i <input_file>')
            sys.exit()
        elif opt in ("-i", "--i_file"):
            input_file = arg

    if len(input_file) > 0:
        print('Input file is: ', input_file)
        if check_file_format(input_file):
            print('Input is a image file')
            data = decode_code(input_file)
            db = database.Database()

            if data >= 0:
                db.select_from(data)
    else:
        print('No input file was given. Try -h for help')


if __name__ == "__main__":
    main(sys.argv[1:])
