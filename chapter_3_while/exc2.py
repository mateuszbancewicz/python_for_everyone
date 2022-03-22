"""
Coin flipper
"""

import random


def coin_flipper():
    flips = 1
    head = 0
    tails = 0
    while flips <= 100:
        coin = random.randint(1, 2)
        match coin:
            case 1:
                head += 1
            case 2:
                tails += 1
        flips += 1
    return f'There were {head} heads and {tails} tails'


if __name__ == '__main__':
    print('Press ENTER to start coin flipper')
    input()
    print(coin_flipper())
    print('\nPress ENTER to exit...')
    input()
