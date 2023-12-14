from gear.armure import Armor
from characters.barbarian import Barbarian
from gear.weapon import Magic,Weapon
import tourpartour

class Wizzard:
    def __init__(self,name,hp,weapon,mana,level):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.mana= mana
        self.level= level

    def stat (self):
        print('name :',self.name)
        print('hp :',self.hp)
        print('weapon:',self.weapon)
        print('mana:',self.mana)
        print('level',self.level)
 
 
    def attackwizzard(enemy):
        Barbarian.health - Magic.damage
        Wizzard.mana - 10
        if Wizzard.mana <= 0:
            print('Vous n\avez plus de mana')
            Barbarian.health - Weapon.damage
        print('il lui reste {Barbarian.health} de point de vie')
        

   
    
    

    
    


