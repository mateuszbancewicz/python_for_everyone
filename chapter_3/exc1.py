"""
Fortune cookie
"""

import random


def fortune_cookie(num):
    match num:
        case 1:
            return 'You will be rich'
        case 2:
            return 'You will be happy'
        case 3:
            return 'You will have luck'
        case 4:
            return 'You will meet someone'
        case 5:
            return 'You will live long'


if __name__ == '__main__':
    print(fortune_cookie(random.randint(1, 5)))
