import os
import sys
import locale
import ghostscript
from PIL import Image
import pyzbar.pyzbar as pyzbar


# folder for temporary files
tmp_dir = "/tmp/"


# file variables
file_ext = ["pdf", "png", "jpg", "jpeg", "tiff", "tif"]


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


def encode_document():
    pass


def identify_document():
    pass


def register_document():
    pass


def entity_linkage():
    pass


def version_history():
    pass


def get_information():
    return "hey"


def update_information():
    pass


def delete_information():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
