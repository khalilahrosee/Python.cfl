import random
import time


class Superhero:
    def __init__(self, name, energy, strength):
        self.name = name
        self.energy = energy
        self.strength = strength

    def attack(self, opponent):
        damage = random.randint(1, self.strength)
        opponent.energy -= damage
        print(f"{self.name} uses their powers and attacks {opponent.name}, dealing {damage} damage!")

    def is_alive(self):
        return self.energy > 0


class Greengoblin:
    def __init__(self, name, energy, strength):
        self.name = name
        self.energy = energy
        self.strength = strength

    def attack(self, opponent):
        damage = random.randint(1, self.strength)
        opponent.energy -= damage
        print(f"{self.name} uses their power and attacks {opponent.name}, dealing {damage} damage!")

    def is_alive(self):
        return self.energy > 0


def main():
    print("Welcome to Superhero vs Green Goblin!")
    print("The hero roams the city, looking for villains to stop, when they spot the Green Goblin causing havoc!")

    hero_name = input("What is your hero's name? ")
    power = input("Choose your power: Frost wave, Lava rumble, or Super punch: ").strip().lower()

    if power in ["frost wave", "lava rumble", "super punch"]:
        print("Good choice! You can now fight the Green Goblin!")
    else:
        print("That is not a valid power, so Super punch will be used by default.")
        power = "super punch"

    hero = Superhero(hero_name, 100, 10)
    goblin = Greengoblin("Green Goblin", 100, 8)

    print("The battle begins!")

    while hero.is_alive() and goblin.is_alive():
        hero.attack(goblin)
        time.sleep(1)

        if not goblin.is_alive():
            break

        goblin.attack(hero)
        time.sleep(1)

    if hero.is_alive():
        print(f"{hero.name} wins! The Green Goblin has fallen.")
    else:
        print(f"{goblin.name} wins! {hero.name} has been defeated.")


main()





