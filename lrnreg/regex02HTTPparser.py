#!/usr/bin/env python3

import re

import requests

def main():

    while True: 
        count =0
        print("Where should we search?")

        url = input("> ")
    
        print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
        searchFor = input("> ")

        resp = requests.get(url)
        searchMe = resp.text
        print(type(searchMe))
        if re.search(searchFor, searchMe):
            print("Found a match!")
            for x in searchMe.split(): 
                if x == searchFor: 
                    count+=1
            print(f"There are {count} occurances of that term")
        else: 
            print("No match!")

        
        contQ = input("Would you like to search again? (enter q if no): ")
        if contQ == 'q':
            break

if __name__ == "__main__":
    main()
