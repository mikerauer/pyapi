#!/usr/bin/python3

import requests
import json
import pprint

#call this API
#api.open-notify.org/astro.json
openapi = "http://api.open-notify.org/astros.json"

def astrocall():
    iss = requests.get(openapi)
    return iss.json()

def main():
    #calls the API and prints to screen with pretty print
    astros = astrocall()
    pprint.pprint(astros)
   
    #creates JSON string....changes list of dict into a JSON String
    #jsonstring = json.dumps(astros)
    #print(jsonstring)

    #write json to file
    with open(astros.json, 'w') as astrofile:
        nauts = astrofiles.write()



#error handle

main()
