"""
WORDS RANDOMIZER
"""

import random


def random_words(words: list):
    while len(words) != 0:
        word = random.choice(words)
        print(word)
        words.remove(word)


WORDS = ['kaczka', 'pietruszka', 'pieczarka', 'yyy... mleko']

if __name__ == '__main__':
    random_words(WORDS)
