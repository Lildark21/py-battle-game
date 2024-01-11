class Barbarian:
    def __init__(self,name, hp, weapon,armor):
        self.name = name
        self.hp= hp
        self.weapon = weapon
        self.armor = armor

 
    def is_alive(self):
        return self.hp> 0


    def attack(self, enemy):
        enemy.armor.defense -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.hp} de point de vie à la sorcière")

    def attack_hp(self, enemy):
        enemy.hp -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.hp} de point de vie à la sorcière")

    def equip_armor(self,armor):
        self.armor = armor 

    def double_attack(self, enemy):
        self.attack(enemy)
        self.attack(enemy)
