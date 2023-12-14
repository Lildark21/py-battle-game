# Supposons que vos classes de personnages soient définies dans un fichier nommé 'personnages.py' dans un dossier nommé 'dossier'
from characters.barbarian import Barbarian
from characters.wizzard import Wizzard


def choisir_personnage():
    personnages = [Barbarian(), Wizzard()]
    print("Voici les personnages disponibles :")
    for i, personnage in enumerate(personnages):
        print(f"{i+1}. {personnage.nom}")
    while True:
        try:
            choix = int(input("Entrez le numéro du personnage que vous voulez choisir : ")) - 1
            if 0 <= choix < len(personnages):
                print(f"Vous avez choisi {personnages[choix].nom}!")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

choisir_personnage()