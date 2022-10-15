import random

def  guess_number_game():

    won = False
    number = random.randint(1, 10)

    while (not won):
        guess = input("Guess the nubmer from 1 to 10:_")
        while not guess.isdigit():
            guess = input("Error - please input a number: ")

        if number == int(guess):
            print("Congratulations - you won! The secret number is", number)
            won = True

guess_number_game()