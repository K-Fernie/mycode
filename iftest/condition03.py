#!/usr/bin/env python3

def main():

    #gather information from the user
    hostname = input("What value should we set for hostname?")

    #set conditional print based on mtg as the host name
    if hostname.lower() == "mtg": 
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    #inform user that script is exiting
    print("Exiting the script...")

main()


