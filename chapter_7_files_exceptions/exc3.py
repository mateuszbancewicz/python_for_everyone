from chapter_7_files_exceptions.exc1 import open_file, next_line, next_block


def generate_player():
    print('Kim jesteś? Podaj imię: ', end=' ')
    player = input()
    return player


def show_scores():
    try:
        with open('last5.txt', 'r', encoding='utf8') as last5:
            try:
                print('\t\t Poprzednie wyniki:')
                score = last5.readline().replace('\n', '')
                print(f'\t\t {score}')
                counter = 1
                score = last5.readline().replace('\n', '')
                while score != '' and counter < 5:
                    print(f'\t\t {score}')
                    score = last5.readline().replace('\n', '')
                    counter += 1
            except EOFError:
                pass
    except FileNotFoundError:
        pass


def welcome(title, player):
    """Przywitaj gracza i pobierz jego nazwę."""
    print(f"\t\t Witaj w turnieju wiedzy, {player}!\n")
    show_scores()
    print(f"\t\t {title} \n")


def score_saver(score, player):
    with open('last5.txt', 'a+', encoding='uft8') as last5:
        last5.write(f'{player}: {score}\n')


def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    player = generate_player()
    welcome(title, player)
    score = 0

    # pobierz pierwszy blok
    category, question, answers, correct, value, explanation = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(value)
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, correct, value, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)

    score_saver(score=score, player=player)


if __name__ == '__main__':
    main()
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
