# Creation d'une classe arme
class Weapon:
    def __init__(self, name, damage, level) :
        self.name = name
        self.damage = damage
        self.level = level
# Creation de des déga sur un enemy
    def actack(self, enemy):
        enemy.life -= self.damage
        
axe = Weapon ('Hacha a 2 main', 5)



# creation de la classe magie le barbare ne peut pas utilisé
class Magic:
    def __init__(self, name, damage, level, mana, drop):
        self.name = name
        self.damage = damage
        self.level = level
        self.mana = mana
        self.drop = drop
        
# Creation de des déga sur un enemy
    def actack(self, enemy):
        enemy.life -= self.damage

wand = Magic ('La baguette de sureau', 10000)