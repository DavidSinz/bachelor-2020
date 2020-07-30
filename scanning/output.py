import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


# print a list to console
def print_list(data):
    for d in data:
        print(d)


# print a given value to console
def print_data(data):
    if type(data) is list:
        print_list(data)
    else:
        print(data)


# detailed information for debugging purpose
def debug(msg):
    logging.debug(msg)
    print(msg)


# information about working processes
def info(msg):
    logging.info(msg)
    print(msg)


# something unexpected happened, program continues running
def warning(msg):
    logging.warning(msg)
    print(msg)


# more serious error prevents an execution of a function
def error(msg):
    logging.error(msg)
    print(msg)


# serious error may cause the program to stop
def critical(msg):
    logging.critical(msg)
    print(msg)
