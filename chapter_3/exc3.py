"""
Guess the number
"""

import random


def guess_the_number(guess):
    tries = 1
    the_number = random.randint(1, 10)
    while guess != the_number:
        if tries == 10:
            return 'Your reach your tries limit'

        if the_number < guess:
            tries += 1
            print('Your number is too high')
            print('\nThe number is...')
            guess = int(input())

        if the_number > guess:
            tries += 1
            print('Your number is too small')
            print('\nThe number is...')
            guess = int(input())
    return f'YAY!! Great, you guess the number in {tries} tries.\nThe numer is {guess}.'


if __name__ == '__main__':
    print('\tWelcome to the game: "Guess the Number"!')
    print('\nI have number in my mind from 1 to 10.')
    print('Guess it. You have 10 tries.')
    print('\nThe number is...')
    first_guess = int(input())
    print(guess_the_number(guess=first_guess))
