import random
from gear.armure import Armor
from characters.wizzard import Wizzard
from characters.barbarian import Barbarian
from gear.weapon import Weapon, Magic
from characters.enemy import Orc

Iron = Armor('Iron',75,"Rare")
Diamond= Armor("Diamond",100,"Epic")
Netherite = Armor("Netherite", 150,"Legendary")
axe = Weapon ('Hacha a 2 main', 30)
wand = Magic('La baguette de sureau', 10, 100, 0.01)

marie = Wizzard('marie',100,wand,Iron,100,1)

Thor= Barbarian('Thor', 200, axe, Iron)

ListArmor = [Iron.defense,Diamond.defense,Netherite.defense]

WizzardArmor = marie.hp + random.choice(ListArmor) 
ThorArmor = Thor.health + random.choice(ListArmor)



    

while marie.hp> 0 and Thor.health > 0:
    marie.attack(Thor)

    if Thor.health <= 0:
        print("Marie à gagné")

    Thor.attack(marie)

    if marie.hp <= 0:
        print('Thor a gagné')





 
 


    


