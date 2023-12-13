import random
from armure import armor
from wizzard import Wizzard
from barbarian import Barbarian
from weapon import Weapon
from weapon import Magic

Iron = armor('Iron',75,"Rare")
Diamond= armor("Diamond",100,"Epic")
Netherite = armor("Netherite", 150,"Legendary")
axe = Weapon ('Hacha a 2 main', 30)
wand = Magic('La baguette de sureau', 1000, 100, 50, 0.01)

marie = Wizzard('marie',100,wand.damage,100,1)

barbarian = Barbarian('Bob le tueur', 200, axe.damage, 'Amure de fer', 1)

ListArmor = [Iron.defense,Diamond.defense,Netherite.defense]

WizzardArmor = marie.hp + random.choice(ListArmor) 
BarbarianArmor = barbarian.hp + random.choice(ListArmor)


def attackbarbarian(self,damage):
    WizzardArmor-Weapon.damage + Weapon.damage
    print(WizzardArmor)
def attackwizzard(self,damage):
    BarbarianArmor-wand.damage
    marie.mana - 10
    print(BarbarianArmor)
    


while WizzardArmor> 0 and BarbarianArmor> 0:
    marie.attackwizzard(BarbarianArmor)

    if BarbarianArmor <= 0:
        print("Marie à gagné")

    BarbarianArmor.attackbarbarian(WizzardArmor)

    if WizzardArmor <= 0:
        print('Barbarian a gagné')





 
 


    


