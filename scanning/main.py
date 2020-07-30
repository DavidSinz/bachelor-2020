# !/usr/bin/python

# import modules
import sys
from PIL import Image
from pyzbar.pyzbar import decode
# import ghostscript

# import custom
from log import Log
from console_controller import ConsoleController

log = Log()


# check for valid code format
# a valid format is: 'CODE:' followed by any number as id
# for example this is valid: 'CODE:001' or 'CODE:6462'
def code_is_valid(code):
    if code is not None and code[0:5].upper() == 'CODE:':
        return True
    return False


# decode a marker of a given input file
def decode_code(file_name):
    # the decode() returns a object with different options to choose from
    # use "log.display(code_object)" for more information
    code_object = decode(Image.open(file_name))
    code = str(code_object.data.decode("utf-8"))
    if code_is_valid(code):
        return code
    return None


# check the file format of a given input file
def file_format_is_supported(file_name):
    try:
        Image.open(file_name)
        return True
    except Exception as e:
        log.display(e)


def convert_pdf_to_jpg(file_name):
    # if file_name.lower().endswith('.pdf'):
    #    return 'pdf'
    # # this is a wrapper function for the actual conversion function
    # try:
    #     args = ["pef2jpeg",  # actual value doesn't matter
    #             "-dNOPAUSE",
    #             "-sDEVICE=jpeg",
    #             "-r144",
    #             "-sOutputFile=" + to_convert,
    #             original]
    #  #     encoding = locale.getpreferredencoding()
    #     args = [a.encode(encoding) for a in args]
    #  #     ghostscript.Ghostscript(*args)
    #     log.info('Donewith pdf to png conversion')
    #     data = decode_code(to_convert)
    #     db = database.Database()
    # except Exception as e:
    #     print(e)
    #     sys.exit()
    pass


def main(argv):
    controller = ConsoleController(argv)

    pass


if __name__ == "__main__":
    main(sys.argv[1:])
