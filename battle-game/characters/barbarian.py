class Barbarian:
    
# Initialise les points de vie, nom arme et armure
    def __init__(self,name, hp, weapon,armor):
        self.name = name
        self.hp= hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, opponent):
        total_attack_power = self.attack_power 
        for _ in range(2):
            if opponent.is_alive():
                opponent.armor.defense -= total_attack_power
                print (f"{self.name} attacks x2{opponent.name} for {total_attack_power} damage! ")
            else:
                break

    def equip_weapon(self,weapon):
        self.weapon =weapon

    def is_alive(self):
        return self.hp> 0

# Attack son adversaire et enleve   
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
