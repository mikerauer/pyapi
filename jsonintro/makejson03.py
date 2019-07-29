#!/usr/bin/python3

# JSON is part of the Python Standard Lib"
import json

def main():
    #open file
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    # display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Pythong cannot easily work with this data.")
    input("Press Enter to continue\n")

    #Create the JSON string
    datacenterdecoded = json.loads(datacenterstring)

    # This is now a Dict
    print(type(datacenterdecoded))

    #display the servers in the datacenter
    print(datacenterdecoded)

    #display row 3
    print(datacenterdecoded["row3"])

    #display 2nd server in  row 2
    print(datacenterdecoded["row2"][1])

    #displays last server in row 3
    print(datacenterdecoded["row3"][-1])


main()    
