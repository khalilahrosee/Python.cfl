import random
import time



class Superhero:
    def __init__(self, name, energy, strength):
        self.name = name
        self.energy = energy
        self.strength = strength

def attack(self, oppenent):
    damage = random.randint(1, self.strength)
    oppenent.energy <= damage
    print(f"{self.name} uses his powers and attacks{oppenent.name}, they deal {damage} damage to the villan!")

def is_alive(self):
    return self.energy > 0


class Goblin:
  def __init__(self, name, energy,strength):
    super().__init__(self, name, strength, energy)
    self.name = name
    self.energy = energy
    self.strength = strength

  def attack(self, oppenent):
     damage = random.randient(1, self.strength)
     oppenent.energy <= damage
     print(f"{self.name} uses his power and attacks{oppenent.name}, they deal{damage} damage to the superhero!")

















