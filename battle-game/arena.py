import random
from characters.enemy import Goblin, Cyclope, Minotaure, Smaug, Orc

class Room:
    def __init__(self, enemy):
        self.enemy = enemy

class Map:
    def __init__(self, rooms):
        self.rooms = rooms

class Salle_1(Room):
    def __init__(self):
        print('Vous entrez dans la salle 1')
        # Faire les ennemies rendomme
        EnemyClass = random.choice(enemy_classes)
        super().__init__(EnemyClass(f"Enemy in Salle_1"))

class Salle_2(Room):
    def __init__(self):
        print('Vous entrez dans la salle 2')
        EnemyClass = random.choice(enemy_classes)
        super().__init__(EnemyClass(f"Enemy in Salle_2"))

class Salle_Boss(Room):
    def __init__(self):
        print('Vous entrez dans la salle du boss')
        super().__init__(Dragon("Smaug est là"))

class Dragon(Smaug):
    pass

enemy_classes = [Orc, Goblin, Cyclope, Minotaure]

salle_1 = Salle_1()
salle_2 = Salle_2()


salle_boss = Salle_Boss()

rooms = [salle_1, salle_2, salle_boss]


map = Map(rooms)

for room in map.rooms:
    print(f"Vous entrez dans une salle et vous voyez un {room.enemy.name}.")