import logging


class Log:

    # display a given string in the terminal
    @staticmethod
    def display(data):
        logging.basicConfig(filename='test.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        print(data)

    # display a given list in the terminal
    @staticmethod
    def display_list(data):
        if type(data) is not list:
            raise ValueError("Input data is not of type list")
        for d in data:
            print(d)
