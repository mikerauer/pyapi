#!/usr/bin/python3

# YAML is not part of the standard lib
#python3 -m pip install pyyaml
import yaml

def main():
    ##create a blob of data to work with
    hitchhikers = [{"name": "Z B", "species": "B"}, \
            {"name": "A D", "species": "H"}]
    
    ##display our Python data (a list containing two dict)
    print(hitchhikers)

    ## create a file o write out to called galaxyguide.yaml
    with open("galaxyguide.yaml", "w") as ggyaml:
        # yaml has not dumps just dump
        yaml.dump(hitchhikers, ggyaml)

main()


