from gear.armure import Armor
from characters.barbarian import Barbarian
from gear.weapon import Magic,Weapon,Spell
from characters.enemy import Orc


class Wizzard:
    def __init__(self,name,hp,weapon,armor,mana,level,spell):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.mana= mana
        self.level= level
        self.spell =spell

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
        choice_atk = input('1. attaquer avec l\'arme - 2. attaquer avec un sort : ')
        
        if choice_atk == "1":
            enemy.armor.defense -=self.weapon.damage
            print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
            print(f'il reste {enemy.armor.defense} à {enemy.name}')
        if choice_atk == "2":
            if self.mana <= 0:
                print('Vous n\'avez plus de mana')
                return choice_atk
            enemy.armor.defense -= self.spell.damage
            self.mana -= self.spell.mana
            print(f'il vous reste {self.mana} de mana')
            print(f"{self.name} attacks {enemy.name} for {self.spell.damage} damage!")
            print(f'il reste {enemy.armor.defense} point d\'armure à {enemy.name}')
            
        


        
        
       


    def attack_hp(self, enemy):
        choice_atk = input('1. attaquer avec l\'arme - 2. attaquer avec un sort : ')
        
        if choice_atk == "1":
            enemy.hp -=self.weapon.damage
            print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
            print(f'il reste {enemy.hp} hp à {enemy.name}')
        if choice_atk == "2":
            if self.mana <= 0:
                print('Vous n\'avez plus de mana')
                print('Vous ne pouvez plus utiliser de sort')
                return choice_atk
            enemy.hp -= self.spell.damage
            self.mana -= self.spell.mana
            print(f'il reste {enemy.hp} hp à {enemy.name}')
            if self.mana <= 0:
                print('Vous n\'avez plus de mana')
                print('Vous ne pouvez plus utiliser de sort')
                return choice_atk
            print(f'il vous reste {self.mana} de mana')
            print(f"{self.name} attacks {enemy.name} for {self.spell.damage} damage!")
       
    


        
    
        

   
    
    

    
    


