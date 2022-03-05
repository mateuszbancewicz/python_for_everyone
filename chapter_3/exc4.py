"""
Computer will guess the number
"""

import random


def correctness(guess, the_number, tries):
    print(f'I guess it is {guess}\nAm I correct?\n')
    print('Y(yes) or N(no)')
    correctness = input().upper()

    if correctness == 'N' and guess != the_number:
        print("Damn it. I will try again\n")
        return False

    elif correctness == 'N' and guess == the_number:
        return 'Hey, you know that I can say when you are cheating?'

    elif correctness == 'Y' and guess != the_number:
        return 'Hey, why are you lying?'

    elif correctness == 'Y':
        return f'YAY!! I guess the number in {tries} tries.\nThe numer is {guess}'


def guess_the_number(the_number):
    tries = 1
    guess = random.randint(1, 2)
    result = correctness(guess=guess, the_number=the_number, tries=tries)
    if result:
        return result

    while tries != 10:
        tries += 1
        guess = random.randint(1, 10)
        result = correctness(guess=guess, the_number=the_number, tries=tries)
        if not result:
            continue
        return result
    return 'I reach tries limit ;('


if __name__ == '__main__':
    print('\tWelcome to the game: "I guess the Number"!')
    print('\nYou write the number and I try to guess.')
    print('I have 100 tries.')
    print('Write down the number between 1 and 10')
    the_number = int(input())
    print(guess_the_number(the_number=the_number))
