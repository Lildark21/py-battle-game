from gear.armure import Armor
from characters.barbarian import Barbarian
from gear.weapon import Magic,Weapon
from characters.enemy import Orc

class Wizzard:
    def __init__(self,name,hp,weapon,armor,mana,level):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.mana= mana
        self.level= level

    def stat (self):
        print('name :',self.name)
        print('hp :',self.hp)
        print('weapon:',self.weapon)
        print('armor', self.armor)
        print('mana:',self.mana)
        print('level',self.level)

    def equip_armor(self,armor):
        self.armor = armor
    
    def equip_weapon(self,weapon):
        self.weapon =weapon
  
    def attack(self, enemy):
        enemy.armor.defense -=self.weapon.damage
        self.mana - self.weapon.mana
        print(f'il vous reste {self.mana} de mana')
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f'il reste {enemy.armor.defense} de point darmure à {enemy.name}')


    def attack_hp(self, enemy):
        enemy.hp -= self.weapon.damage
        self.mana -self.weapon.mana
        print(f'il vous reste {self.mana} de mana')
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f'il reste {enemy.hp} de point de vie à {enemy.name}')
    
        

   
    
    

    
    


