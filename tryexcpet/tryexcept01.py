#!/usr/bin/python3

while True:
    try:

        #pull info from user

        name = input('Enter a file name: ')
        with open(name, 'w') as myfile:
            myfile.write('well done\n')
    except:
        print('EH EH EH, you didn\'t say the magic word')
    else:
        print('Yeah, you\'re not an idiot.')
        break
