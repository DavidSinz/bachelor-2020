# !/usr/bin/python

# import modules
import sys
import os
import getopt
import log
from PIL import Image
from pyzbar.pyzbar import decode
# import ghostscript
import locale

# import custom
import database


# it runs from main function after program receives image file it decodes barcode data.
def decode_code(file_name):
    log.info('Barcode decoding is done here')
    data_objects = decode(Image.open(file_name))
    doc_id = -1

    for obj in data_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data)
        doc_id = str(obj.data.decode("utf-8"))

    return doc_id


# when you press 'a' in cmd this function runs to register new file/doc.
def register_doc():
    entry1 = input('code_id: ')
    entry2 = input('file_name: ')
    entry3 = input('Path: ')
    entry4 = input('insert_date: ')

    entry5 = input('creation_date: ')
    entry6 = input('date_of_update: ')
    entry7 = input('date_of_last_access: ')
    entry8 = input('file_type: ')
    entry9 = input('size: ')
    entry10 = input('attribute: ')
    entry11 = input('optionsText: ')

    d = database.Database()
    d.insert_into(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11)
    log.info('Values being entered into the database')


# this contain industry level ghostscript to convert pdf to png , Reference : ActiveState.com
def pdf_to_image(original, to_convert):
    # this is a wrapper function for the actual conversion function
    try:
        args = ["pef2jpeg",  # actual value doesn't matter
                "-dNOPAUSE",
                "-sDEVICE=jpeg",
                "-r144",
                "-sOutputFile=" + to_convert,
                original]

        encoding = locale.getpreferredencoding()
        args = [a.encode(encoding) for a in args]

        ghostscript.Ghostscript(*args)
        log.info('Donewith pdf to png conversion')
        data = decode_code(to_convert)
        db = database.Database()

        if data != None and data[0:5].upper() == 'CODE:':

            check_lst = db.select_from(data)
            log.info('Step to find the QR code in db.')

            if check_lst == []:
                print('\nNo data available for this code in db')
            else:
                print(check_lst)
        else:
            print('File has no or invalid barcode.')
            print('Register this file in db whatsoever\n')
            log.info('File has no or invalid barcode.')
            register_doc()
    except Exception as e:
        print(e)
        sys.exit()


# this function runs from the lines b/w 175 to 195 of main function,it checks the file format
def check_file_format(file_name):
    try:
        Image.open(file_name)
        log.info('Image is being processed in the check file format function')
        return True

    except Exception as e:
        print(e)
        if file_name.lower().endswith('.pdf'):
            changed_filename = file_name.replace('.pdf', '.png')

            pdf_to_image(file_name, changed_filename)
            log.info('Conversion of pdf to png starts')


# this is the main function for the command line's opt of deleting file
def file_del(file):
    try:
        file_name = 'C:/Users/Moiz/PycharmProjects/BarCodeExtractor/' + file
        os.remove(file_name)
        log.info('File deleted with the name')
    except PermissionError and FileNotFoundError:
        print('This file is open somewhere else or there is no such file')


def main(argv):
    # This is the main and the first function to be run from here.

    input_file = ''
    # intitalizing all the commands usable in cmd
    try:
        opts, args = getopt.getopt(argv, 'hi:aud:sv:f:', ['', 'i_file=', 'delete_query=', 'view_by_id', 'file_del'])
    # exception if the command is not in the recorded list
    except getopt.GetoptError:
        log.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        log.warning('You are using any wrong command')
        print('this is a wrong command,refer to help(-h)\n')
        sys.exit(2)
    # below all the functionalities of the commands have explained
    for opt, arg in opts:
        # help function
        if opt in ['-h']:
            print('usage: main.py -i <input_file>')
            print('usage: main.py -a adds to database')
            print('usage: main.py -u  updates the database')
            print('usage: main.py -d  <give_id_to_delete_records>')
            print('usage: main.py -s view every record')
            print('usage: main.py -v <qrcode_to_view>')
            print('usage: main.py -f <input_file_to_delete>')

            sys.exit()
        # file_input

        elif opt in ("-i", "--i_file"):

            input_file = arg
            log.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
            log.info('Input file command is executed successfully')
        # adding records to database
        elif opt in ('-a'):
            register_doc()

        # updating data base function
        elif opt in ['-u']:
            query = input('Query?: ')
            d = database.Database()
            d.update(query)
            log.info('Update query executed')
        # to delete any record in the database
        elif opt in ['-d', '--delete_query']:
            d = database.Database()
            d.delete(arg)
            log.warning('The values corresponding to this id have been deleted permanently')
        # viewing records of database
        elif opt in ['-s']:

            d = database.Database()
            d.select_all()
        # viewing records by particular id
        elif opt in ['-v', '--view_by_id']:
            db = database.Database()
            c = db.select_from(arg)
            print(c)
        # deleting any file functionality
        elif opt in ['-f', '--file_del']:
            file_del(arg)

    # Line 175 to 195 checks if there is file if the file is valid if it's pdf so it is converted to png and then data corresponding to the file is displayed!

    if len(input_file) > 0:
        print('Input file is: ', input_file)
        log.info('The file being inputted is eligible')
        if check_file_format(input_file):
            log.info('The file has the correct format')
            print('Input is a image file')
            data = decode_code(input_file)
            db = database.Database()

            if data != None and data[0:5].upper() == 'CODE:':

                check_lst = db.select_from(data)
                log.info('Step to find the QR code in db.')

                if check_lst == []:
                    print('\nNo data available for this code in db')
                else:
                    print(check_lst)
            else:
                print('File has no or invalid barcode.')
                print('Register this file in db whatsoever\n')
                log.info('File has no or invalid barcode.')
                register_doc()


    # this runs after the command is finished executing
    else:
        print('\nProgram Ends, -h for more commands')
        log.info('The command executed successfully')


if __name__ == "__main__":
    # just a reminder
    print('\n', '*' * 30, 'Disclaimer', '*' * 30)
    print('\nKeep the file to be uploaded in the same folder or give the full path here.\n')
    main(sys.argv[1:])
