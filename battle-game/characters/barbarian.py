class Barbarian:
    def __init__(self,name, hp, weapon,armor):
        self.name = name
        self.hp= hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, opponent):
        total_attack_power = self.attack_power
        if self.weapon is not None:
            total_attack_power += self.weapon.damage
        for _ in range(2):
            if opponent.is_alive():
                opponent.hp -= total_attack_power
                print (f"{self.name} attacks {opponent.name} for {total_attack_power} damage!")
            else:
                break

    def is_alive(self):
        return self.hp> 0


    def attack(self, enemy):
        enemy.armor.defense -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.armor.defense} de point d'armure  à la sorcière")

    def attack_hp(self, enemy):
        enemy.hp -= self.weapon.damage
        print(f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
        print(f"il reste {enemy.hp} de point de vie à la sorcière")

    def equip_armor(self,armor):
        self.armor = armor 
