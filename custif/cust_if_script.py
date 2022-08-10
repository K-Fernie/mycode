#!/usr/bin/env python3

def main():

    grade = int(input("Please enter the score you recieved on the paper: "))

    if grade >= 90:
        print("You earned an A")
    elif grade >= 80: 
        print("You earned a B")
    elif grade >= 70: 
        print("You earned a C")
    elif grade >= 60: 
        print("You earned a D")
    else: 
        print("You need to study more... F")

main()
