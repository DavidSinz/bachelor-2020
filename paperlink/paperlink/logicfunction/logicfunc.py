import os
import sys
import locale
import datetime
import ghostscript
from PIL import Image
import pyzbar.pyzbar as pyzbar

from datamanager.datamngr import DataManager


# folder for temporary files
tmp_dir = "/tmp/"


# file variables
file_ext = ["pdf", "png", "jpg", "jpeg", "tiff", "tif"]


# presentation variables
display_data = """id, name, path, size, type, dumped, file_type, link_id, set_id"""


# datamanager variables
dmgr_data_keys = """id, name, path, code, link_id, set_id, size, type, 
                 insert_date, dumped, data_name, file_type"""


def register_print_document(source_path):
    try:
        if not _is_file_path_valid(source_path):
            raise Exception
        if not _is_file_format_supported(source_path):
            raise Exception
    except:
        print("Invalid input")
    else:
        dmgr = DataManager()
        db_data = {}
        db_data["id"] = dmgr.get_next_free_index()
        db_data["name"] = os.path.basename(source_path)
        db_data["path"] = source_path
        db_data["set_id"] = _generate_set_id(dmgr, source_path)
        db_data["link_id"] = _generate_link_id(dmgr, db_data["set_id"])
        db_data["code"] = _generate_code(db_data["link_id"], db_data["set_id"])
        db_data["size"] = os.path.getsize(source_path)
        db_data["type"] = "print"
        db_data["insert_date"] = str(datetime.datetime.now())
        db_data["dumped"] = 0
        db_data["data_name"] = f"data{db_data['id']}"
        db_data["file_type"] = os.path.splitext(source_path)[1][1:]
        dmgr.save_document(db_data)
        dmgr.save_doc_copy(db_data["id"], source_path)


def register_scan_document(source_path):
    doc = Image.open(source_path)
    code = _decode_marker(doc)
    if _is_print_still_saved(code):
        if _is_scan_already_saved(code):
            print("Scan document is already saved in database")
        else:
            try:
                if not _is_file_format_supported(source_path):
                    raise Exception
            except:
                print("The document format is not supported")
            else:
                dmgr = DataManager()
                db_data = {}
                db_data["id"] = dmgr.get_next_free_index()
                db_data["name"] = os.path.basename(source_path)
                db_data["path"] = source_path
                db_data["code"] = code
                db_data["set_id"] = int(code.split(":")[2])
                db_data["link_id"] = int(code.split(":")[1])
                db_data["size"] = os.path.getsize(source_path)
                db_data["type"] = "scan"
                db_data["insert_date"] = str(datetime.datetime.now())
                db_data["dumped"] = 0
                db_data["data_name"] = f"data{db_data['id']}"
                db_data["file_type"] = os.path.splitext(source_path)[1][1:]
                dmgr.save_document(db_data)
                dmgr.save_doc_copy(db_data["id"], source_path)
    else:
        print("Print document is not saved anymore")


def get_entity_linkage_by_doc_id(doc_id):
    dmgr = DataManager()
    code = dmgr.get_code_of_document(doc_id)
    print_doc = dmgr.get_print_doc_by_code(display_data, code)
    scan_doc = dmgr.get_scan_doc_by_code(display_data, code)
    return [_tupel_to_dict(print_doc), _tupel_to_dict(scan_doc)]


def get_version_history_by_doc_id(doc_id):
    dmgr = DataManager()
    code = dmgr.get_code_of_document(doc_id)
    docs = dmgr.get_documents_by_set_id(int(code.split(":")[2]), display_data)
    for i in range(len(docs)):
        docs[i] = _tupel_to_dict(docs[i])
    docs = sorted(docs, key=lambda doc: doc["type"])
    docs = sorted(docs, key=lambda doc: doc["link_id"])
    result = []
    group = []
    for d in docs:
        if len(group) == 0 and d["type"] == "scan":
            group.append(None)
            group.append(d)
            result.append(group)
            group = []
        elif len(group) == 0 and d["type"] == "print":
            group.append(d)
        elif len(group) == 1 and d["type"] == "scan":
            group.append(d)
            result.append(group)
            group = []
        elif len(group) == 1 and d["type"] == "print":
            group.append(None)
            result.append(group)
            group = []
            group.append(d)
    for r in result:
        r = _tupel_to_dict(r)
    return result


def update_document(doc_id, source_path):
    if os.path.isfile(source_path):
        dmgr = DataManager()
        db_data = {}
        db_data["name"] = os.path.basename(source_path)
        db_data["path"] = source_path
        db_data["size"] = os.path.getsize(source_path)
        db_data["file_type"] = os.path.splitext(source_path)[1][1:]
        dmgr.update_document(doc_id, db_data)


def dump_document(doc_id):
    dmgr = DataManager()
    dmgr.update_document(doc_id, {"dumped": 1})


def delete_document(doc_id):
    dmgr = DataManager()
    dmgr.delete_doc_copy(doc_id)
    dmgr.delete_document(doc_id)


def _is_file_path_valid(source):
    return True


def _is_print_still_saved(code):
    print(code)
    dmgr = DataManager()
    data = dmgr.get_all_documents("*", f"code = '{code}' AND type = 'print'")
    print(data)
    if len(data) > 0:
        return True
    return False


def _is_scan_already_saved(code):
    dmgr = DataManager()
    data = dmgr.get_all_documents("*", f"code = '{code}' AND type = 'scan'")
    if len(data) > 0:
        return True
    return False


def _generate_link_id(dmgr, set_id):
    data = dmgr.get_documents_by_set_id(set_id, "*")
    if len(data) > 0:
        return dmgr.get_next_free_link_id(set_id)
    return 0


def _generate_set_id(dmgr, source_path):
    data = dmgr.get_documents_by_path(source_path)
    if len(data) > 0:
        return data[0][5]
    return dmgr.get_next_free_set_id()


def _generate_code(link_id, set_id):
    return f"PL:{link_id}:{set_id}"


def _is_file_format_supported(source_path):
    if os.path.splitext(source_path)[1][1:] in file_ext:
        return True
    return False


def _decode_marker(image):
    result = []
    try:
        code_object = pyzbar.decode(image)
    except Exception as e:
        print(f"Could not decode marker. Error: {e}")
    else:
        for obj in code_object:
            result.append(obj.data)
    return result[0].decode("utf-8")


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


# The next section is for functions, which prepare the document data for the
# display in the presentation layer.

def _tupel_to_dict(data):
    dict_keys = display_data.split(", ")
    dict_keys = [d.strip() for d in dict_keys]
    result = []
    for i in range(len(data)):
        result.append(dict_keys[i])
        result.append(data[i])
    return {result[i]: result[i + 1] for i in range(0, len(result), 2)}


def _process_data_to_dict_array():
    dmgr = DataManager()
    data = dmgr.get_all_documents(display_data)
    for i in range(len(data)):
        data[i] = _tupel_to_dict(data[i])
    return data


def get_all_documents_presentation():
    data = _process_data_to_dict_array()
    result = []
    for d in data:
        if d["dumped"] == 0:
            result.append(d)
    return result


def get_print_documents_presentation():
    data = _process_data_to_dict_array()
    result = []
    for d in data:
        if d["type"] == "print" and d["dumped"] == 0:
            result.append(d)
    return result


def get_scan_documents_presentation():
    data = _process_data_to_dict_array()
    result = []
    for d in data:
        if d["type"] == "scan" and d["dumped"] == 0:
            result.append(d)
    return result


def get_dumped_documents_presentation():
    data = _process_data_to_dict_array()
    result = []
    for d in data:
        if d["dumped"] == 1:
            result.append(d)
    return result


def get_doc_information_presentation(doc_id):
    data = {
        "linkage": get_entity_linkage_by_doc_id(doc_id),
        "version": get_version_history_by_doc_id(doc_id)
    }
    return data


def main():
    pass


if __name__ == "__main__":
    main()
