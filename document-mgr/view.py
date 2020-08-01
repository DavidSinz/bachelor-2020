class View:

    def __init__(self, log_level):
        self.log_level = log_level

    # detailed information for debugging purpose
    def debug(self, msg):
        print(msg)

    # information about working processes
    def info(self, msg):
        print(msg)

    # something unexpected happened, program continues running
    def warning(self, msg):
        print(msg)

    # more serious error prevents an execution of a function
    def error(self, msg):
        print(msg)

    # serious error may cause the program to stop
    def critical(self, msg):
        print(msg)
