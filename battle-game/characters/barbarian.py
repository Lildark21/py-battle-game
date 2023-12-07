class Barbarian:
    def __init__(self, name, hp, weapon, armor, level):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.level = level
    
    def feature(self):
        print('name:', self.name) 
        print('hp:', self.hp)
        print('weapon:', self.weapon)
        print('armor:', self.armor)
        print('level:', self.level)
        
barbarian = Barbarian('Bob', 200, 'Hache a 2 main', 'Amure de fer', 1)

barbarian.feature()
