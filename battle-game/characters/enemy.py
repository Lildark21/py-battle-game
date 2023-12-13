import random
from gear.weapon import Weapon
from gear.armor import Armor

class Orc:
    def __init__(self, name, health=380, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

    def drop_item(self):
        drop_rate = random.random()
        if drop_rate < 0.5:
            return Weapon('Hacha a 2 main', 30)
        else:
            return Armor('Armure de cuir', 50)

# Création d'un orc
orc = Orc("Gruumsh")
# L'orc laisse tomber un objet
item = orc.drop_item()
print(item)
