#!/usr/bin//env python3

# Created on: September 2019
# Created by: Paul Madut
# This is the a program used as a random number generator


import random


def main():
    # This function does plays a game

    # Input
    random_number = random.randint(0, 9)
    number_guessed = int(input("Enter a number to play: "))
    print(" ")

    # Process
    if number_guessed == random_number:
        print("Congrats you right dawg.")

    else:
        print("You are a failure.")


if __name__ == "__main__":
    main()
