import getopt


class ConsoleController:

    def __init__(self, argv):
        # init all the usable commands
        try:
            opts, args = getopt.getopt(argv, 'hi:aud:sv:f:', ['', 'i_file=', 'delete_query=', 'view_by_id', 'file_del'])
        # exception if the command is not in the recorded list
        except getopt.GetoptError:
            sys.exit(2)

        # below all the functionalities of the commands have explained
        for opt, arg in opts:
            # help function
            if opt in ['-h']:
                print('usage: main.py -i <input_file>')
                print('usage: main.py -a adds to database')
                print('usage: main.py -u  updates the database')
                print('usage: main.py -d  <give_id_to_delete_records>')
                print('usage: main.py -s view every record')
                print('usage: main.py -v <qrcode_to_view>')
                print('usage: main.py -f <input_file_to_delete>')

                sys.exit()
            # file_input

            elif opt in ("-i", "--i_file"):

                input_file = arg
                log.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                log.info('Input file command is executed successfully')
            # adding records to database
            elif opt in ('-a'):
                register_doc()

            # updating data base function
            elif opt in ['-u']:
                query = input('Query?: ')
                d = database.Database()
                d.update(query)
                log.info('Update query executed')
            # to delete any record in the database
            elif opt in ['-d', '--delete_query']:
                d = database.Database()
                d.delete(arg)
                log.warning('The values corresponding to this id have been deleted permanently')
            # viewing records of database
            elif opt in ['-s']:

                d = database.Database()
                d.select_all()
            # viewing records by particular id
            elif opt in ['-v', '--view_by_id']:
                db = database.Database()
                c = db.select_from(arg)
                print(c)
            # deleting any file functionality
            elif opt in ['-f', '--file_del']:
                file_del(arg)

        # Line 175 to 195 checks if there is file if the file is valid if it's pdf so it is converted to png and then data corresponding to the file is displayed!

        if len(input_file) > 0:
            print('Input file is: ', input_file)
            log.info('The file being inputted is eligible')
            if check_file_format(input_file):
                log.info('The file has the correct format')
                print('Input is a image file')
                data = decode_code(input_file)
                db = database.Database()

                if data != None and data[0:5].upper() == 'CODE:':

                    check_lst = db.select_from(data)
                    log.info('Step to find the QR code in db.')

                    if check_lst == []:
                        print('\nNo data available for this code in db')
                    else:
                        print(check_lst)
                else:
                    print('File has no or invalid barcode.')
                    print('Register this file in db whatsoever\n')
                    log.info('File has no or invalid barcode.')
                    register_doc()


        # this runs after the command is finished executing
        else:
            print('\nProgram Ends, -h for more commands')
            log.info('The command executed successfully')

    def input_file(self):
        pass

    def display_all_files(self):
        pass

    def delete_file(self):
        pass

