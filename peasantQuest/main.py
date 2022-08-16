#!/usr/bin/env python3

from art import *
import os
from travelAnimation import load_animation
#from B3 import peasantHome
from globalInfo import complexInstructions, introText


def main():

    #initial introduction to PeasCant Quest
    tprint("PeasCant Quest", font="epic",chr_ignore=True)
    print(complexInstructions)

    startGame = input("Are you ready to begin the quest?? y/n: ")

    #TODO - Grab game information from CSV file and determine if they want to load save information 
    if startGame.lower() == "y":
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print(introText)

        mv = input("\nPress ENTER to BEGIN\n")
        if(mv.lower() != "q"):
            os.system("clear")
            load_animation("Awaaaay we goooo....")
            #TODO - uncomment this  code when you are ready to test, right now building out the bones
            #peasantHome()
            
    else: 
        print("Come back again... if you are peasanty enough!!")

if __name__ == "__main__":
    main()
