"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marie Koblížková
email: mariekoblizkova@seznam.cz
"""

import random

oddelovac = "_" *55
hra_bezi = True

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.")

def random_number():
    digits = "0123456789"
    random_digits = random.sample(digits, 4)

    while random_digits[0] == '0':
        random_digits = random.sample(digits, 4)

    return ''.join(random_digits)

tajne_cislo = random_number()
# print(tajne_cislo)

print("Let's play a bulls and cows game.")
print(oddelovac)
print("Enter a number:")
print(oddelovac)

def get_input_number():
    input_number = input(" ")
    while len(set(input_number)) != 4 or any(digit not in "0123456789" for digit in input_number) or input_number[0] == "0":
        print("Invalid input.")
        input_number = input(" ")
        print(oddelovac)

    return input_number
   

def prubeh_hry():
    hra_bezi = True
    guesses = 0
    while hra_bezi:
        bulls = 0
        cows = 0
        guesses += 1

        current_input = get_input_number()
        for i in range(4):
            if current_input[i] == tajne_cislo[i]:
                bulls += 1
            elif current_input[i] in tajne_cislo:
                cows += 1
        print(f"Bulls: {bulls}")
        print(f"Cows: {cows}")

        if bulls == 4:
            hra_bezi = False
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(oddelovac)
            print("That's amazing!")
        else:
            print(oddelovac)

prubeh_hry()


