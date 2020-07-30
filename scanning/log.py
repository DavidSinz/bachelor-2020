import logging


class Log:

    # display a given string in the terminal
    @staticmethod
    def display(data):
        print(data)

    # display a given list in the terminal
    @staticmethod
    def display_list(data):
        if type(data) is not list:
            raise ValueError("Input data is not of type list")
        for d in data:
            print(d)
