#!/usr/bin/env python3

import crayons
import json

def devicereboot(iplist):
    for ip in iplist:
        print(f'Connecting to... {ip}\nREBOOTING NOW!')


def commandpush(devicecmd):

    for ip in devicecmd.keys():
        
        print(f'{crayons.red("Handshaking")}..... connecting with {id}')
        
        for mycmds in devicecmd[ip]:
            print(f"Attempting to sending command ---> {mycmds}")

    return None


def main():
    """called at runtime"""
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)
   
    print(f"Welcome to the {crayons.blue('Network ')}Device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)
    devicereboot(devicecmd.keys())

main()


