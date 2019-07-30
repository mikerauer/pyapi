#!/usr/bin/python

import sys

#start with inf loop
while True:
    try:
        z ='"Successful job'
        print('lets divide x by y!')
        x = int(input('Value for x?'))
        y = int(input('Value for y?'))
        print('The value of x/y: ', x/y)
    except ZeroDivisionError as zerr:
        print('Handling of a run time error: ', zerr)
        z = 'Error div by zero'
    except ValueError as err:
        z = 'Value Error detected vis user input'
    except:
        print('Oh look that was dumb')
        print(sys.exc_info()[0])
        z = sys.exc_info()[0]
        raise
    finally:
        with open('try02.log', 'w') as log:
            log.append(str(z)+'\n')

            #still needs a keyboard intercept handling....
