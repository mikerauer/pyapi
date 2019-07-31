#!/usr/bin/python3

###########################still broken

import json
import requests
import pprint

x = 'y'
url = 'https://www.anapioficeandfire.com/api/books/'

def whichbook():
    # input from user for which book #
    booknum = input('Which book number in the series would you like to see the ISBN? ')
    return booknum

def apicall(booknum):
    # calls API and returns json
    got = requests.get(url + booknum)
    return got.json()

def main():
    # prints ISBN number to screen
    while True:
        try:
            # book number
            book = whichbook()
            # api call
            thrones = apicall(book)
            # prints ISBN
            print(thrones['isbn'])
            # asks user if they want to continue
            x = input('Would you like to check another? y/n ')
            # check if you said n and breaks
            if x.lower() == 'n':
                break
        except KeyboardInterrupt:
            # all specific errors need to be above the catch all
            # allows ctrl-c to get out at any point
            break
        except:
                # response if book number wasnt in the list
                print('Book number not in the list')

main()
