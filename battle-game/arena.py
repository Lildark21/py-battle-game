import random
from characters import enemy

class Room:
    def __init__(self, enemy):
        self.enemy = enemy

class Map:
    def __init__(self, rooms):
        self.rooms = rooms

# Liste des classes d'ennemis
enemy_classes = [Orc, Goblin, Cyclope, Minotaure]

rooms = []

for i in range(10):
    if i == 9:  # La dernière salle contient le boss
        enemy = Smaug("Smaug")
    else:  # Les autres salles contiennent un ennemi aléatoire
        EnemyClass = random.choice(enemy_classes)
        enemy = EnemyClass("Enemy")
    rooms.append(Room(enemy))

map = Map(rooms)

# Maintenant, vous pouvez itérer sur map.rooms pour combattre chaque ennemi
for room in map.rooms:
    print(f"Vous entrez dans une salle et vous voyez un {room.enemy.name}.")
    # Ici, vous pouvez ajouter la logique pour le combat
