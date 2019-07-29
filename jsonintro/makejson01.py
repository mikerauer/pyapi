#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "Zaphod beeblebrox", "species": "betelgeusian"},\
            {"name": "Arther Dent", "species": "Human"}]
    print(hitchhikers)
    
    #zfile = open("galaxyguide.json", "w")  #needs to be closed

    with open("galaxyguide.json", "w") as zfile:  #no need to close
        json.dump(hitchhikers, zfile)  #json.dump(input data, file like object)
    
    #zfile.close()

main()
