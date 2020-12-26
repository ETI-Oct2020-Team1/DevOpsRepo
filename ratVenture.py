#ratVenture.py
from ratVentureMenus import *
import random

main = Menu()
choice = main.main_menu()

while choice != 0:
    if choice == 1:
        townChoice = main.town_menu()
    # elif choice == 2:
        #Enter code for resume game
    # else:
        #Enter code for Exit Game
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