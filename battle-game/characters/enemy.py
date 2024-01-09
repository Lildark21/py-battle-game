import random
from gear.weapon import Weapon
from gear.armure import Armor


class Orc:
    def __init__(self, name, health=880, attack_power=10,):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
        
class Goblin:
    def __init__(self, name, health=100, attack_power=5 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
class Cyclope:
    def __init__(self, name, health=150, attack_power=20 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
class Minotaure:
    def __init__(self, name, health=100, attack_power=30 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

# boss
class Smaug:
    def __init__(self, name, health=500, attack_power=50):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
