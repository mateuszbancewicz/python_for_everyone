# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

class Critter:
    """Wirtualny pupil"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            mood = "zadowolony"
        elif 11 <= unhappiness <= 15:
            mood = "podenerwowany"
        else:
            mood = "wściekły"
        return mood

    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()

    def eat(self, food):
        print("Mniam, mniam.  Dziękuję.")
        for _ in range(food // 2):
            self.__pass_time()
        self.hunger -= food
        self.hunger = max(self.hunger, 0)

    def play(self, fun):
        print("Hura!")
        for _ in range(fun // 2):
            self.__pass_time()
        self.boredom -= fun
        self.boredom = max(self.boredom, 0)

    def __str__(self):
        rep = f'''
        Nazywam się {self.name}
        Mój poziom niezadowolenia: {self.boredom}
        Mój poziom głodu: {self.hunger}
'''
        return rep


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)

        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()

        # nakarm swojego zwierzaka
        elif choice == "2":
            food = int(input('Podaj ilość porcji: '))
            crit.eat(food=food)

        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            having_fun = int(input("Ile zabaw wymyśliłeś/aś dla zwierzaka: "))
            crit.play(fun=having_fun)

        elif choice == '99':
            print(crit)

        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
