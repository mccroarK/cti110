# This program generates a random number and asks the user to guess the number.
# 10/24/2019
# CTI-110 P5HW1 - Random Number
# Kevin McCroary
# 

import random

# Constants for min and max
MIN = 1
MAX = 100

# Constants for menu options
PLAY_GAME = 1
EXIT = 2

# Main function
def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = int(input('Enter your choice: '))
        if choice == PLAY_GAME:
            rngenerator()
        elif choice == EXIT:
            print('Exiting the program')
        else:
            print('\nError: invalid selection\n')

# Function that displays the menu.
def display_menu():
    print('MAIN MENU')
    print('\n-------------------\n')
    print(' 1) Play game')
    print(' 2) Exit')

# Random number generator
def rngenerator():
    random_num = random.randint(MIN, MAX)
    guess_num = 0
    while guess_num != random_num:
        guess_num = int(input('\nEnter your guess: '))
        if guess_num < random_num:
            print('Too low, try again.')
        elif guess_num > random_num:
            print('Too high, try again.')
        else:
            print('Good job!\n')
main()

# create menu and ask for user input (1 = play, 2 = quit)
# function generates random numbers on input of 1
# let user guess and give hint on failure
