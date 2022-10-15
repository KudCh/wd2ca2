import random

def  guess_number_game(start, stop):

    won = False
    number = random.randint(start, stop)

    while (not won):
        guess = input("Guess a nubmer from "+str(start)+" to "+str(stop)+":_")
        while not guess.isdigit():
            guess = input("Error - please input a number: ")

        guess = int(guess)

        if number < guess:
            print("The secret number is less than ", guess)
            guess_number_game(start, guess)

        elif number > guess:
            print("The secret number is greater than ", guess)
            guess_number_game(guess, stop)

        elif number == guess:
            print("Congratulations - you won! The secret number is", number)
            won = True
    return

guess_number_game(1, 10)