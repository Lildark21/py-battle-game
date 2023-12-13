from characters.barbarian import Barbarian
from gear.weapon import Weapon
from gear.armure import Armor
from characters.enemy import Orc



weapon = Weapon("Hach a 2 mains", 30)
barbarian = Barbarian("Bob le tueur", weapon=weapon)
enemy = Orc("Orc")

while barbarian.is_alive() and enemy.is_alive():
    barbarian.attack(enemy)
    if enemy.is_alive():
        enemy.attack(barbarian)

winner = barbarian if barbarian.is_alive() else enemy
print(f"The winner is {winner.name}!")