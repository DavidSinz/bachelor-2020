import os, time
import shutil
import pathlib
from stat import * # ST_SIZE etc



class FileManager:

    #==========================================================================
    #
    # class 'FileManager'
    #
    # This class handles files. It copies files and saves them to a given
    # location. It also deletes files.
    #
    
    stat_names = ("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime")

    #==========================================================================
    #
    # constructor '__init__'
    #
    # The constructor sets the class variable directory, which stores
    # information about the folder location, where files will be stored.
    #

    def __init__(self, data_dir):
        self.data_dir = data_dir

    #==========================================================================
    #
    #
    #

    def extract_file_information(self, file_path):
        result = {}
        try:
            stat = os.stat(file_path)
        except IOError:
            print("failed to get information about ", file_path)
            return None
        else:
            for i in range(len(stat)):
                result[self.stat_names[i]] = str(stat[i])
            return result

    #==========================================================================
    #
    # 'save_file_to_data_dir'
    #
    # The method 'save' copies a given file to a specified directory. The
    # file will be saved under the given file name.
    #

    def save_file_to_data_dir(self, source, file_name):
        shutil.copy(source, self.data_dir + file_name)
        return 

    #==========================================================================
    #
    # 'delete_data_from_data_dir'
    #
    # The method 'delete' deletes a file from the specified directory.
    #

    def delete_data_from_data_dir(self, file):
        # remove(self.data_dir + file)
        pass

