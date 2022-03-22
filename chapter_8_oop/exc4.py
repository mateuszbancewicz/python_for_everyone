# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować
import random


class Critter:
    """Wirtualny pupil"""

    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.boredom = random.randint(0, 10)

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
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.")
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


def critter_farm(quantity):
    critters_list = []
    for _ in range(quantity):
        critter_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
        critter = Critter(name=critter_name)
        critters_list.append(critter)
    return critters_list


def main(critters_list):
    quantity = len(critters_list)
    choice = None
    while choice != "0":
        print("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj swoich zwierzaków
        2 - nakarm swoje zwierzaki
        3 - pobaw się ze swoimi zwierzakami
        """)

        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            for critter in critters_list:
                critter.talk()

        # nakarm swojego zwierzaka
        elif choice == "2":
            food = int(input('Podaj ilość porcji: '))
            for critter in critters_list:
                critter.eat(food=food)

        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            having_fun = int(input("Ile zabaw wymyśliłeś/aś dla zwierzaków: "))
            for critter in critters_list:
                critter.play(fun=having_fun)

        elif choice == '99':
            for critter in critters_list:
                print(critter)

        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


if __name__ == '__main__':
    how_many = int(input('Podaj ilość zwierzaków: '))
    critters = critter_farm(quantity=how_many)
    main(critters_list=critters)
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

