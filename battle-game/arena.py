import random
from characters.enemy import Goblin
from characters.enemy import Cyclope
from characters.enemy import Minotaure
from characters.enemy import Smaug
from characters.enemy import Orc

class Room:
    def __init__(self, enemy):
        self.enemy = enemy

class Map:
    def __init__(self, rooms):
        self.rooms = rooms

class Salle_1(Room):
    pass

class Salle_2(Room):
    pass


enemy_classes = [Orc, Goblin, Cyclope, Minotaure]


for Salle in [Salle_1, Salle_2]:
    EnemyClass = random.choice(enemy_classes)
    enemy = EnemyClass(f"Enemy in {Salle.__name__}")
    Salle.enemy = enemy

class Salle_Boss(Room):
    pass

class Dragon(Smaug):
    pass

salle_1 = Salle_1(random.choice(enemy_classes)(f"Enemy in Salle_1"))
salle_2 = Salle_2(random.choice(enemy_classes)(f"Enemy in Salle_2"))

# Ajoutez le boss à la salle du boss
salle_boss = Salle_Boss(Dragon("Smaug est là"))

rooms = [salle_1, salle_2, salle_boss]

for i in range(3):
    EnemyClass = random.choice(enemy_classes)
    enemy = EnemyClass(f"Enemy {i}")
    rooms.append(Room(enemy))

map = Map(rooms)

for room in map.rooms:
    print(f"Vous entrez dans une salle et vous voyez un {room.enemy.name}.")

