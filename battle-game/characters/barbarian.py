from gear.weapon import Weapon
from gear.armor import Armor
from characters.enemy import Orc

class Barbarian:
    def __init__(self, name, health=50, attack_power=20, weapon=None, armor=None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon
        self.armor = armor

    def attack(self, opponent):
        total_attack_power = self.attack_power
        if self.weapon is not None:
            total_attack_power += self.weapon.damage
        opponent.health -= total_attack_power
        print (f"{self.name} attacks {opponent.name} for {total_attack_power} damage!")

    def is_alive(self):
        return self.health > 0

axe = Weapon('Hacha a 2 main', 30)
leather_armor = Armor('Armure de cuir', 50)
barbarian = Barbarian("Bob le tueur", weapon=axe, armor=leather_armor)
