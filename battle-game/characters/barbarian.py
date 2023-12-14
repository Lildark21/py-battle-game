from gear.weapon import Weapon
from gear.armure import Armor
from characters.enemy import Orc

class Barbarian:
    def __init__(self,name, health, weapon,armor):
        self.name = name
        self.health = health
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


    def attack(self, enemy):
        enemy.hp -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")

