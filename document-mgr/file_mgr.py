from os import remove
from shutil import copy


class FileManager:

    ##########################################################################
    #
    # Class FileManager
    #
    # This class handles files. It copies files and saves them to a given
    # location. It also deletes files.
    #

    ##########################################################################
    #
    # '__init__'
    #
    # The constructor sets the class variable directory, which stores
    # information about the folder location, where files will be stored.
    #

    def __init__(self, directory):
        self.directory = directory

    ##########################################################################
    #
    # 'save'
    #
    # The method 'save' copies a given file to a specified directory. The
    # file will be saved under the given file name.
    #

    def save(self, source, file):
        copy(source, self.directory + file)

    ##########################################################################
    #
    # 'delete'
    #
    # The method 'delete' deletes a file from the specified directory.
    #

    def delete(self, file):
        remove(self.directory + file)
