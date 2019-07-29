#!/usr/bin/python3

def main():
    hostipdict = {'host01': '192.168.3.4', 'host02': '192.168.3.3', 'host03': '192.168.2.3'}
    
    print(hostipdict)

    print(hostipdict['host02'])

    hostipdict['host4'] = '192.168.0.9'  #add host to dict

    print(hostipdict)

    hostipdict.update({'host05': '9.9.3.4'})  #add host to dict

    print(hostipdict)

    print(hostipdict.get('host66'))  #.get returns no index erros
#    hostipdict['host66']      # returns index error (keyerror)

    print(hostipdict.keys())
    print(hostipdict.values())
   

main()
