#!/usr/bin/env python3
import random
import os 

#Game function
def guessinit(guessWord, guessPhrase):

    userAttempts = 0

    while userAttempts < 3:
        if userAttempts == 2:
            print("This is your last chance")

        usrGuess = input(f"Enter the last Word of the title '{guessPhrase}' : ")
        if usrGuess.lower() == guessWord.lower():
            print(f"Correct the movie title is: '{guessPhrase} {guessWord}'")
            break
        else:
            left = 3 - (userAttempts + 1)
            print(f"Incorrect you have {left} more chances")
            userAttempts+=1

#Phrase Generator for the game
def generatePhrase(): 
    #List of movies to randomly pull a phrase from
    montyPythonMovies = ["The Meaning of Life", "The Holy Grail", "The Life of Brian", "Flying Circus"]
    #Item returned from the random choice
    movie = random.choice(montyPythonMovies)
    return movie

def runGame():
    userRes = input("Would you like to start a game? y/n: ")
    if userRes.lower() == "y": 
        return True
    else: 
        return False

#Function at runtime
def main():
    playAgain = runGame()
   
    while playAgain:
        os.system("clear")
        #Generate Random choice from the list of movies
        movie = generatePhrase()
   
        #Determine Guess Word
        guessBuild = movie.split()
        guessWord = guessBuild.pop()
        #Determine guess phrase
        guessPhrase = " ".join(guessBuild)
    
        guessinit(guessWord, guessPhrase)
        playAgain = runGame()

    print("Thanks for playing")

main()

