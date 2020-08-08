##############################################################################
#
# Implemented with: Python 3.7
# Used modules: logging, pathlib, sqlite3, sys
#

from sys import argv
import getopt
import configparser

from program.model.programmodel import Model


def init_model(config):
    model = Model(config)


def init_controller(config, args):
    pass


def init_view(config):
    pass


##############################################################################
#
# Main method which handles the all running processes
#

def main(args):


    config = configparser.ConfigParser()
    print()
    config.read('../config.ini')

    init_model(config)
    init_controller(config, args)
    init_view(config)

    inputfile = ""
    try:
        opts, args = getopt.getopt(argv, "hi:d:")
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')

        elif opt in "-i":
            inputfile = arg
        elif opt in "-d":
            delet = ""
    print('Input file is "', inputfile)


if __name__ == "__main__":
    main(argv[1:])
