class Barbarian:
    
# Initialise les points de vie, nom arme et armure
    def __init__(self,name, hp, weapon,armor):
        self.name = name
        self.hp= hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy):
        enemy.armor.defense -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.armor.defense} de point d'armure à {enemy.name}")
        enemy.armor.defense -= self.weapon.damage
        print(f'{self.name} attack aggain {enemy.name}')
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        enemy.armor.defense -= self.weapon.damage
        print(f"il reste {enemy.armor.defense} de point d'armure à {enemy.name}")


    def attack_hp(self, enemy):
        enemy.hp -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.hp} hp à {enemy.name}")
        enemy.hp -= self.weapon.damage
        print(f'{self.name} attack aggain {enemy.name}')
        enemy.armor.defense -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.hp} hp à {enemy.name}")

    def equip_weapon(self,weapon):
        self.weapon =weapon

    

# Attack son adversaire et enleve   
    

    def equip_armor(self,armor):
        self.armor = armor 

    
