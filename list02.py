#!/usr/bin/python3

def main():
    list = ['cisco', 'juniper', 'big_ip', 'tellabs', 'meraki']

    print(list[2])

    list.append('nortel')

    print(list[-1])

#   list.extend("what")  #adds to list, each letter
    list2 = ['a', 'bb', 'cc']
    list.extend(list2) #combines lists
    print(list)

main()
