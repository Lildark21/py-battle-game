from gear.armure import Armor
from characters.barbarian import Barbarian


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
 
 
    def attackwizzard(self,damage):
        Barbarian.health - self.weapon
        print(Barbarian.health)
        

   
    
    

    
    


