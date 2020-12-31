from RatVentureFunctions import * 
#ratVenture.py

from ratVentureMenus import *
import random

main = Menu()

while choice != 0:
    if choice == 1:
        townChoice = main.town_menu()
    elif choice == 2:
        #Enter code for Resume
        pass
    else:
        #Enter code for exiting game
        pass
    choice = 0

while townChoice != 0:
    if townChoice == 1:
        # Enter code for viewing character
        pass
    # elif townChoice == 2:
        # Enter code for viewing map
    elif townChoice == 3:
        # Enter code for moving + map
        combatChoice = main.combat_menu()
    # elif townChoice == 4:
        # Enter code for Rest
    # elif townChoice == 5:
        # Enter code for saving game
    else:
        # Enter code for exiting game
        pass
    townChoice = 0


while combatChoice != 0:
    if combatChoice == 1:
        damage = random.randint(1,3)
        print(f'\nYou deal {damage} damage to the Rat')
        # ---- To implement editing of RatHP - damage properly ----
        if RatHP == 0:
            print("The Rat is dead! You are victorious!")
            outdoorChoice = main.outdoor_menu()
        else:
            RatHP = RatHP - damage
            main.combat_menu()
    else:
        print("\nYou run and hide.")
        outdoorChoice = main.outdoor_menu()
    combatChoice = 0


while outdoorChoice != 0:
    if outdoorChoice == 1:
        # Enter code for view character
        pass
    # elif outdoorchoice == 2:
        # Enter code for viewing map
    elif outdoorChoice == 3:
        # Enter code for moving + map
        combatChoice = main.combat_menu()
    else:
        # Enter code for exiting game
        pass
    outdoorChoice = 0

def run():
    world = World()
    
    ### Player must always be initialized first
    player = GameEntity(world, "The Hero",[2,4],1,20)
    rat = GameEntity(world,"A rat",[0,0],1,20)
    
    world.add_entity(player)
    world.add_entity(rat)

    print(player.name)
    print(player.id)
    print(player.attack)
    print(player.hp)
    print(rat.id)
    damage(player,rat)
    main_menu()

while True:
    run()
