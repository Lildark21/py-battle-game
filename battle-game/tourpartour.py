import random
from gear.armure import Armor
from characters.wizzard import Wizzard
from characters.barbarian import Barbarian
from gear.weapon import Weapon, Magic
from characters.enemy import Orc


axe = Weapon ('Hacha a 2 main', 30)
wand = Magic('La baguette de sureau', 10, 100, 0.01)
 
marie = Wizzard('marie',100,wand,None,100,1)
Thor= Barbarian('Thor', 200, axe, None)






def choose_character():
    
    print("choose a character")
    print("1. Sorcière")
    print("2. Barbare")
   
    choose_character = input("Choisisser votre personage  : ")




    if choose_character == "1":
        wand = Magic('La baguette de sureau', 10, 100, 0.01)
 
        marie = Wizzard('marie',100,wand,None,100,1)
       
        print('vous avez choisi marie')
        # print(f'le barbare est lenemy')
        return marie
        
        
        
    elif choose_character == "2":
        axe = Weapon ('Hacha a 2 main', 30)
        Thor= Barbarian('Thor', 200, axe, 0)
       
        print('Vous avez choisi Thor')
        return Thor
        
    else:
        return(choose_character)

# if choose_character == 1:
#     enemy = Thor.hp
#     print("okay mon truf")
# if choose_character == 2:
#     enemy = marie.hp
#     print("win")

    
def choose_armor():

    print("Choisisser une armure")
    print("1. Fer") 
    print("2. Diamond")
    print("3. Netherite")
    
    choose_armor = input("Choisisser votre armure  :")
    Iron = Armor('Iron',75,"Rare")
    Diamond= Armor("Diamond",100,"Epic")
    Netherite = Armor("Netherite", 150,"Legendary")
    ListArmor = [Iron.defense,Diamond.defense,Netherite.defense]
    
    if choose_armor == "1":
        print('Vous avez choisi larmure en fer')
        return Iron
    elif choose_armor =="2":
        print('Vous avez choisi larmure de diamand')
        return Diamond
        
        
    elif choose_armor =="3":
        print('Vous avez choisi larmure de Netherite')
        return Netherite
    else:
        return(choose_armor)
    
    

   


    
def choose_enemy():
    marie = Wizzard('marie',100,wand, None,100,1)
    Thor= Barbarian('Thor', 200, axe, None)
    print("1. Marie")
    print("2. Thor")
    choose_enemy = input("Choisisser votre enemy  : ")
    

    if choose_enemy == "1":
        print("vous allez combattre marie")
        return marie
    elif choose_enemy == "2":
        print("Vous aller combatre Thor")
        return Thor
    
   
def random_armor():
    Iron = Armor('Iron',75,"Rare")
    Diamond= Armor("Diamond",100,"Epic")
    Netherite = Armor("Netherite", 150,"Legendary")
    ListArmor = [Iron,Diamond,Netherite]
    random_choose_armor = random.choice(ListArmor)
    return random_choose_armor
    

     
enemy = choose_enemy()
enemy_armor = random_armor()

enemy.equip_armor(enemy_armor)

    
character = choose_character()
# print(f"Personnage choisi : {character}")
# print(type(character))
character_armor = choose_armor()
print(character_armor.name)
character.equip_armor(character_armor)
print(enemy.name)
print(character.armor.defense)
print((enemy.armor.defense))



# Enemy.equip_armor(armor)
# # print(f"Armure choisie :{armor}")

# EnemyArmor = Enemy.hp + random.choice(ListArmor)



# characterArmor = character.hp + armor
# print (f' vous avez au total {characterArmor} hp')


while character.armor.defense > 0 and enemy.armor.defense > 0:
   
    character.attack(enemy)
    
    

        
    enemy.attack(character)
    

if character.armor.defense <= 0:
    print('votre armure est cassé')
if enemy.armor.defense <= 0:
    print('vous avez cassé larmure de votre adversaire')

while character.hp > 0 and enemy.hp > 0:

    character.attack_hp(enemy)
    

    enemy.attack_hp(character)



    




 
 


    


