from gear.weapon import Weapon
from characters.enemy import Orc


class Barbarian:
    def __init__(self, name, health=100, attack_power=20, weapon=30):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon

    def attack(self, opponent):
        total_attack_power = self.attack_power
        if self.weapon is 30:
            total_attack_power += self.weapon.power
        opponent.health -= total_attack_power
        print (f"{self.name} attacks {opponent.name} for {total_attack_power} damage!")

    def is_alive(self):
        return self.health > 0


    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")


barbarian = Barbarian("Bob le tueur")

barbarian.feature()
