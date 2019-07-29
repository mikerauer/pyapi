#!/usr/bin/python3

# YAML is not part of the standard lib
#python3 -m pip install pyyaml
import yaml
import json

def main():
    #opens galaxyguide.yaml as read as a var called gg
    with open('galaxyguide.yaml', 'r') as ggyaml:
        # take gg and load it into a yaml named pyyammy
        pyyammy = yaml.load(ggyaml)

    print(pyyammy)

    #appends pyammy with new key/value pair
    pyyammy.append({"name": "P I", "species": "R"})
    
    print(pyyammy)

    with open('galaxyguide.yaml', 'w') as wwjson:
        json.dump(pyyammy, wwjson)    

    
'''
    ##create a blob of data to work with
    hitchhikers = [{"name": "Z B", "species": "B"}, \
            {"name": "A D", "species": "H"}]
    
    ##display our Python data (a list containing two dict)
    print(hitchhikers)

    ## create a file o write out to called galaxyguide.yaml
    with open("galaxyguide.yaml", "w") as ggyaml:
        # yaml has not dumps just dump
        yaml.dump(hitchhikers, ggyaml)
'''
main()


