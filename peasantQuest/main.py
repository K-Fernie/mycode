#!/usr/bin/env python3

from art import *
from PIL import Image
import os
from travelAnimation import load_animation

#Game starts - describes character
#HELP: when typed at any point shows certain commands
#MoveTo: Allows the character to move to a certain point on the map
#Each LOCATION: has certain objectives (that allow the story to progress)
#Hero has items that they must obtain, if item == true then they can do a certain action


def main():

    #TODO - add the map print image somewhere within the view code
    # with Image.open('PythonPeasantQuest\images\peasantmap.png') as img:
    #     img.show()

    tprint("Welcome to PeasCant Quest", font="epic",chr_ignore=True)
    print("GENERAL INSTRUCTIONS\n")
    print("-Look around by typing stuff like 'look tree' or 'look'")
    print("-Talk to folks by typing stuff like 'talk man'")
    print("-Take items by typing 'get(item)'")
    print("-Use items by typing 'use(item)', you can also 'give(item)' and 'throw(item)'")
    print("-Type 'inv' to see your INVENTORY")
    print("-Type 'map' to see your map")
    print("-Type Travel (A1) to travel to a map location")
    print("-Type 'q' at any time to quit")

    startGame = input("Would you like to start a game? y/n: ")
    print("------------------------------------------------")
    #create a gameinit(startGame) function that is called and all the rest of the progress goes from here

    if startGame.lower() == "y":
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("zoned")

        print("\nYou are Rather Dashing, a humble peasant living in the peasant kingdom of Peasantry\n"
        + "You return home from a vacation on Scalding Lake only to find that Trogdor the Burninator " +
        "has burninated your thatched roof cottage along with all your goods and services.\n" +
        "With nothing left to lose, you swear to get revenge on that Wingaling Dragon in the name of burninated peasants everywhere.\n" +
        "You head east towards the mountain atop which NOTTrogdor lives.")
        mv = input("Press ENTER to Continue\n")
        if(mv.lower() != "q"):
            load_animation("Traveling to your peasantly destination.....")
    #TODO - Create a scene change function that shows animation for scene change
    #TODO - Figure out if theres a way to clear the command line
    #TODO - Create different Scenes with objectives. The player will have scene objectives listed in his class and the scene will search for it's objective to determine if the scene is complete

main()
