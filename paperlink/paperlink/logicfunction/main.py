import os
import sys
import locale
import ghostscript
from PIL import Image
import pyzbar.pyzbar as pyzbar

from server import Server

# file variables
file_ext = ["pdf", "png", "jpg", "jpeg", "tiff", "tif"]


# socket information
host = '127.0.0.1'
port = 5500


def _decode_marker(image):
    result = []
    try:
        code_object = pyzbar.decode(image)
    except Exception as e:
        print(f"Could not decode marker. Error: {e}")
    else:
        for obj in code_object:
            result.append(obj.data)
    return result


def _convert_pdf_to_jpeg(pdf_file, jpeg_file):
    args = ["gs",
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r144",
            "-sOutputFile=" + jpeg_file,
            pdf_file]
    try:
        encoding = locale.getpreferredencoding()
        args = [a.encode(encoding) for a in args]
        ghostscript.Ghostscript(*args)
    except Exception as e:
        print(f"The conversion from pdf to image failed. Error: {e}")


def _is_file_format_supported(file_name):
    name, ext = os.path.splitext(file_name)
    print(ext)


def get_code_value_of_document(input_file):
    pass


def get_path_of_linked_source(doc_id):
    pass


def get_all_documents():
    pass


def main():
    #server = Server(host, port)
    pass


if __name__ == "__main__":
    main()
