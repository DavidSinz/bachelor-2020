# !/usr/bin/python

# import modules
import sys
import time
import getopt
import ntpath

from PIL import Image
from pyzbar.pyzbar import decode

# custom modules
import output
from document import ScanDocument
from database import Database


# check for valid code format
# a valid format is: 'CODE:' followed by any number as id
# for example this is valid: 'CODE:001' or 'CODE:6462'
def code_is_valid(code):
    if code is not None and code[0:5].upper() == 'CODE:':
        return True
    return False


# decode a marker of a given input file
def decode_code(input_file):
    # the decode() returns a object with different options to choose from
    # use "log.display(code_object)" for more information
    code_object = decode(Image.open(input_file))
    code = str(code_object[0].data.decode("utf-8"))
    if code_is_valid(code):
        return code.rsplit(":", 1)[1]
    return None


# check the file format of a given input file
def determine_file_format(input_file):
    file_types = ["pdf", "jpg", "jpeg", "png", "tif", "tiff", "gif", "bmp"]
    for f_type in file_types:
        if input_file.lower().endswith("." + f_type):
            return f_type
    return None


def convert_pdf_to_image(file_name):
    # TODO: implement pdf to image converter here
    pass


# register scan document
def register_input_file(input_file):
    file_format = determine_file_format(input_file)
    if file_format is None:
        output.error("file format is not supported")
    elif file_format is "pdf":
        output.error("pdf files are currently not supported")
    else:
        output.info("decode code if available")
        code = decode_code(input_file)
        if code is not None:
            # create new ScanDocument instance with the input file
            file_path = ntpath.abspath(input_file).rsplit("\\", 1)[0]
            file_name = ntpath.basename(input_file)
            output.debug(file_path)
            output.debug(file_name)
            doc = ScanDocument(code, file_name, file_path, time.strftime('%Y-%m-%d %H:%M:%S'))
            d = Database("tes1")
            d.insert_scan_doc(doc.get_code(), doc.get_file_name(), doc.get_path())
            print(d.select_all_scan_doc())


def main(argv):
    # init all the usable commands
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        output.print_data("invalid command. use -h for help")
        sys.exit(2)
    for opt, arg in opts:
        if opt is "-h":
            output.print_data('test.py -i <input_file>')
            sys.exit()
        elif opt is "-i":
            input_file = arg

    if len(input_file) > 0:
        register_input_file(input_file)
    else:
        output.warning("no file could be accessed")


if __name__ == "__main__":
    main(sys.argv[1:])
