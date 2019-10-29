# This program quizzes users on their ability to add and subtract
# 10/24/2019
# CTI-110 P5HW2 - Math Quiz
# Kevin McCroary
#

import random

MIN = 1
MAX = 100

ADD_NUM = 1
SUB_NUM = 2
EXIT = 3

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = int(input('Enter your choice: '))
        if choice == ADD_NUM:
            add_numbers()
        elif choice == SUB_NUM:
            sub_numbers()
        elif choice == EXIT:
            print('Exiting the program')
        else:
            print('Error: invalid selection.')

def display_menu():
    print('MAIN MENU')
    print('\n------------------')
    print('1) Add Random Numbers')
    print('2) Subtract Random Numbers')
    print('3) Exit')

def add_numbers():
    addnum1 = random.randint(MIN,MAX)
    addnum2 = random.randint(MIN,MAX)
    add_sum = addnum1 + addnum2
    print('\n', addnum1, '+', addnum2, '= ', end='')
    guess_sum = int(input())
    if guess_sum == add_sum:
        print('Congrats!\n')
    else:
        print('The correct answer is: ', add_sum,'\n')

def sub_numbers():
    subnum1 = random.randint(MIN,MAX)
    subnum2 = random.randint(MIN,MAX)
    sub_diff = subnum1 - subnum2
    print('\n', subnum1, '-', subnum2, '= ', end='')
    guess_diff = int(input())
    if guess_diff == sub_diff:
        print('Congrats!\n')
    else:
        print('The correct answer is: ', sub_diff,'\n')

main()

# create menu and rng and ask for input (1 = add, 2 = subtract, 3 = quit)
# generates random numbers to add or subtract
# user has to guess answer and is congratulated on correct answer
