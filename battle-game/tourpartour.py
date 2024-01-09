import random
from gear.armure import Armor
from characters.wizzard import Wizzard
from characters.barbarian import Barbarian
from gear.weapon import Weapon, Magic
from characters.enemy import Orc


axe = Weapon ('Hacha a 2 main', 30)
wand = Magic('La baguette de sureau', 100, 10, 0.01)
sword = Weapon('Epée', 20)
wandfire = Magic('Baguette de feu', 100, 15,0.01)
marie = Wizzard('marie',100,None,None,100,1)
Thor= Barbarian('Thor', 200, None, None)






def choose_character():
    
    print("choose a character")
    print("1. Sorcière")
    print("2. Barbare")
   
    choose_character = input("Choisisser votre personage  : ")




    if choose_character == "1":
        wand = Magic('La baguette de sureau', 100, 10, 0.01)
 
        marie = Wizzard('marie',100,None,None,100,1)
       
        print('vous avez choisi marie')
        # print(f'le barbare est lenemy')
        return marie
        
        
        
    elif choose_character == "2":
        axe = Weapon ('Hacha a 2 main', 30)
        Thor= Barbarian('Thor', 200, None, 0)
       
        print('Vous avez choisi Thor')
        return Thor
        
    else:
        return(choose_character)


    
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


def choose_weapon():
    axe = Weapon ('Hacha a 2 main', 30)
    wand = Magic('La baguette de sureau', 75, 10, 0.01)
    wandfire = Magic('Baguette de feu', 90, 15,0.01)
    sword = Weapon('Epée', 20)
    print('1. axe')
    print('2. épée')
    print('3. Baguette de sureau')
    print('4. Baguette de feu')
    choose_weapon = input('Chosissez votre arme')
    
    if choose_weapon == '1':
        print('vous avez choisi La hache')
        return axe
        
    if choose_weapon == '2':
        print('vous avez choisi une épée')
        return sword
    if choose_weapon == '3':
        print( 'vous avez choisi la baguette de sureau')
        return wand
    if choose_weapon == '4':
        print('vous avez choisi une baguette de feu')
        return wandfire
    
def enemy_weapon():
    axe = Weapon ('Hacha a 2 main', 30)
    wand = Magic('La baguette de sureau', 75, 10, 0.01)
    wandfire = Magic('Baguette de feu', 90, 15,0.01)
    sword = Weapon('Epée', 20)
    Barbarian_weapon = [axe,sword]
    Wizzard_weapon = [wand,wandfire]

    enemy =choose_enemy()
    if enemy.name == 'marie':
        random_wand = random.choice(Wizzard_weapon)
        return random_wand
    if enemy.name == 'Thor':
        random_weapon = random.choice(Barbarian_weapon)
        return random_weapon


     

         
def choose_enemy():
    marie = Wizzard('marie',100,None, None,100,1)
    Thor= Barbarian('Thor', 200, None, None)
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
Weapon_for_enemy = enemy_weapon()

print(Weapon_for_enemy)

enemy.equip_armor(enemy_armor)
character = choose_character()
weapon_for_character = choose_weapon()
character.equip_weapon(weapon_for_character)

enemy.equip_weapon(Weapon_for_enemy)
character_armor = choose_armor()
character.equip_armor(character_armor)
print(character.weapon.name)
print(enemy.weapon)
   
    


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



    




 
 


    


