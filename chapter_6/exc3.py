"""
Guess the number
"""

import random


def display_instructions():
    print('\tWelcome to the game: "Guess the Number"!')
    print('\nI have number in my mind from 1 to 10.')
    print('Guess it. You have 10 tries.')


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def guess_the_number(guess):
    question = '\nThe number is...'
    start = 1
    stop = 10
    tries = 1
    the_number = random.randint(start, stop)
    while guess != the_number:
        if tries == 10:
            return 'Your reach your tries limit'

        if the_number < guess:
            tries += 1
            print('Your number is too high')
            guess = ask_number(question=question, low=start, high=stop)

        if the_number > guess:
            tries += 1
            print('Your number is too small')
            guess = ask_number(question=question, low=start, high=stop)

    return f'YAY!! Great, you guess the number in {tries} tries.\nThe numer is {guess}.'


def main():
    display_instructions()
    print('\nThe number is...')
    first_guess = int(input())
    print(guess_the_number(guess=first_guess))
