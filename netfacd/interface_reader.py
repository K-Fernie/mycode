#!/usr/bin/env python3

import netifaces

def interfaceSearch(intName):
    if intName in netifaces.interfaces():
        return netifaces.ifaddresses(intName)[netifaces.AF_INET][0]['addr']
    else: 
        return "No Interface Exists With That Name"


def macSearch(intName):
    if intName in netifaces.interfaces():
        return netifaces.ifaddresses(intName)[netifaces.AF_LINK][0]['addr']
    else: 
        return "No Interface Exists with that name"


print(netifaces.interfaces())

for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information')


print('\n****************INTERFACE SEARCH: **************************')
intName = input('Please enter the name of the interface to find it\'s associated IP Address:\n')
print(f"IP : {interfaceSearch(intName)} || MAC : {macSearch(intName)}")

        
