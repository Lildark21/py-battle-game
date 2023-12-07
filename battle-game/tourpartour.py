import random
from armure import armor
from wizzard import Wizzard
from barbarian import Barbarian

Iron = armor('Iron',75,"Rare")
Diamond= armor("Diamond",100,"Epic")
Netherite = armor("Netherite", 150,"Legendary")

marie = Wizzard('marie',100,'Baguette magique',100,1)

barbarian = Barbarian('Bob le tueur', 200, 'Hache a 2 main', 'Amure de fer', 1)

ListArmor = [Iron.defense,Diamond.defense,Netherite.defense]

WizzardArmor = marie.hp + random.choice(ListArmor)
BarbarianArmor = barbarian.hp + random.choice(ListArmor)


    


