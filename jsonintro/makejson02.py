#!/usr/bin/python3

import json

def main():
    # list of 2 dict
    hitchhikers = [{"name": "Zaphod beeblebrox", "species": "betelgeusian"},\
            {"name": "Arther Dent", "species": "Human"}]
    print(hitchhikers)
    
    #creates JSON string....changes list of dict into a JSON String
    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)

main()
