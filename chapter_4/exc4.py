import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
word = random.choice(WORDS)
length = len(word)
halp_word = '_' * length
guess = ''
tries = 5

print('\t\tWitaj w grze ZGADNIJ SŁOWO!!!')
print(f"\tDługość wylosowanego słowa wynosi {length} liter")
print('\t\tMasz 5 szans')

while guess != word:
    if guess != word and tries < 5:
        print('Źle\n')
    halp = input('Czy chcesz podać literkę: (Y/N)')
    while halp in ['n', 'y']:
        if halp.lower() == 'n':
            break
        if halp.lower() == 'y':
            letter = input('Odgadnij 1 literke: ').lower()
            for i in range(length):
                if letter == word[i]:
                    halp_word = halp_word[:i] + word[i] + halp_word[i + 1:]
                    print(f"Podpowiedź: {halp_word}")
                    break
                print('Nie ma takiej literki')
                break
        else:
            halp = input('Czy chcesz podać literkę: (Y/N)')
    guess = input('Zgadnij słowo: ')
    tries -= 1

print('Gratulację, zgadłeś!')
