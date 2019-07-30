#!/usr/bin/python3

import uuid

#simulate a job # with uuid package
ticket = uuid.uuid1()

try:
    print('Please type the config file to load')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
except:
    x = "error with obtaining config file info"
else:
    x = "switch file found"
finally:
    with open('try03.log', 'a') as zlog:
        print('\nWriting results of service to log file...')
        print(ticket, ' - ', x, file=zlog)


