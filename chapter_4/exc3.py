import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
    """
               Witaj w grze 'Wymieszane litery'!
    
       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
print("Zgadnij, jakie to słowo:", jumble)


points = len(correct)
letters = ''
guess = input("\nTwoja odpowiedź: ")
i = 0
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    halp = input('Czy chcesz literkę? (Y/N)')

    if halp.lower() == 'y':
        letters += correct[i]
        i += 1
        points -= 1
        print(f'Podpowiedź: {letters}')
    guess = input("Twoja odpowiedź: ")

if guess == correct:
    print("Zgadza się! Zgadłeś!\n")
    print(f'Zdobyłeś {points} punktów')

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
