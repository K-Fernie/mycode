#!/usr/bin/env python3

#Create a list of lists of your favorite foods by adding three lists together
#Print lists
#Then print your favorite food on the list

#Make a dictionary definint three shared qualities of your favorite fictional heroes!
#Print all keys and values seperately.


def main():
    #Create 3 lists of your favorite food
    fav_food1 = ["Pizza", "Beer", "Ramen"]
    fav_food2 = ["Sushi", "Noodles", "Cookies"]
    fav_food3 = ["Natto", "Eggs & Rice", "Cafe Rio Salad"]
    
    #Create a mega list by extending the first list with the two other lists
    fav_food1.extend(fav_food2)
    fav_food1.extend(fav_food3)

    #Iterate over mega list and display all foods
    print("My Favorite foods are as follows")
    for item in fav_food1: 
        print(item)
    #Printing favorite food
    print(f"My Favorite food on that list is {fav_food1[0]}")
    #Adding new line for UX
    print("\n")
    #Create dictionary of heroes
    hero_dict = {"Samwise":
                    {"type":"support",
                    "strength":"Emotional Damage",
                    "weapon": "short sword"}, 
                "Aragorn": {
                    "type": "King", 
                    "strength": "Orc Slaying",
                    "weapon": "long sword and bow"},
                "Gandalf the Grey":{
                    "type":"Wizard", 
                    "strength": "Balrog Slayer", 
                    "weapon": "Magic Staff & Sword"}}

    print("FANTASY HEROES of my childhood are:")
    for hero in hero_dict.keys():
        print(hero)
        print(hero_dict[hero])

main()
