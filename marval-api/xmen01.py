#!/usr/bin/python3

import argparse
import time
import hashlib
import pprint

import requests


##Define the API here
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## Calc a hash to pass thru to our Marvel API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
## Items being passed DO NOT need to match var name in code.
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

##Perform a call to Marvel Char API (timestone, storm, cerebro, lookmeup)
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    deadpool = requests.get(XAVIER + '?name=' + lookmeup + '&ts=' + stampystamp + '&apikey=' + pkeyz + '&hash=' + hashyhash)
    #print(XAVIER+'?name='+lookmeup+'&ts='+stampystamp+'&apikey='+pkeyz+'&hash='+hashyhash)
    return deadpool.json()

def main():
    #harvest priv key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')
    
    #harvest pub key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    # create a RAND by grabbing the current time
    timestone = str(time.time()).rstrip('.')

    # grab a 1 time use has
    cerebro = hashbuilder(timestone, beast, storm)

    ## call the api with marvalcharcall(...)
    uncannyxmen = marvelcharcall(timestone, cerebro, storm, "Wolverine")
    
    ## display results
    print(uncannyxmen['data']['results'][0]['id'])
    print(uncannyxmen['data']['results'][0]['name'])
    print(uncannyxmen['data']['results'][0]['description'])

# only true if python3 invokes the script, import wont fire script
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing the Marvel priv dev key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing the Marvel pub dev key')
    args = parser.parse_args()
    main()
