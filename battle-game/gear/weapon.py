class Weapon:
    def __init__(self, name, damage=30):
        self.name = name
        self.damage = damage

    def attack(self, enemy):
        enemy.life -= self.damage

    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}"

class Magic:
    def __init__(self, name, damage=1000, mana=100, drop=0.001):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.drop = drop

    def attack(self, enemy):
        enemy.life -= self.damage

    def __str__(self):
        return f"Magic: {self.name}, Damage: {self.damage}, Mana: {self.mana}, Drop: {self.drop}"
