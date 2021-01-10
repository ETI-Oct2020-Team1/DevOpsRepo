dayNum = 1

class Menu:
    #UI for Outdoor Menu
    def outdoor_menu(self):
        # print out either the attack or run message
        print("1) View Character")
        print("2) View Map")
        print("3) Move")
        print("4) Exit Game")
        outdoorChoice = 0
        while 1 > outdoorChoice or 4 < outdoorChoice:
            try:
                outdoorChoice = int(input("Enter choice: "))
                #print(f'Choice is {outdoorChoice}')
            except ValueError:
                print("\nPlease input a number between 1-4.")
        outdoor_menu_choices(outdoorChoice)

    #UI for Combat Menu
    def combat_menu(self):
        print("\nDay ",dayNum,": You are out in the open.")
        rat_object()
        print("1) Attack")
        print("2) Run")
        combatChoice = 0
        while 1 > combatChoice or 2 < combatChoice:
            try:
                combatChoice = int(input("Enter choice: "))
                #print(f'Choice is {combatChoice}')
            except ValueError:
                print("\nPlease input a number between 1-2.")
        combat_menu_choices(combatChoice)

    # UI for Town Menu
    def town_menu(self):
        print("\nDay ",dayNum,": You are in a town.")
        print("1) View Character")
        print("2) View Map")
        print("3) Move")
        print("4) Rest")
        print("5) Save Game")
        print("6) Exit Game")
        townChoice = 0
        while 1 > townChoice or 6 < townChoice:
            try:
                townChoice = int(input("Enter choice: "))
                #print(f'Choice is {townChoice}')
            except ValueError:
                print("\nPlease input a number between 1-6.")
        town_menu_choices(townChoice)


    # UI for Main Menu
    def main_menu(self):
        print("Welcome to Ratventure!")
        print("----------------------")
        print("1) New Game")
        print("2) Resume Game")
        print("3) Exit Game")
        choice = 0
        while 1 > choice or 3 < choice:
            try:
                choice = int(input("Enter choice: "))
                #print(f'Choice is {choice}')
            except ValueError:
                print("\nPlease input a number between 1-3.")
        main_menu_choices(choice)

# Function for main menu choices
def main_menu_choices(choice):
    if choice == 1:
        main.town_menu()
    elif choice == 2:
        #Enter code for Resume
        pass
    else:
        #Enter code for exiting game
        pass

# Function for town menu choices
def town_menu_choices(townChoice):
    if townChoice == 1:
        # Enter code for viewing character
        pass
    # elif townChoice == 2:
        # Enter code for viewing map
    elif townChoice == 3:
        # Enter code for moving + map
        main.combat_menu()
    # elif townChoice == 4:
        # Enter code for Rest
    # elif townChoice == 5:
        # Enter code for saving game
    else:
        # Enter code for exiting game
        pass

# Function for combat menu choices
def combat_menu_choices(combatChoice):
    if combatChoice == 1:
        damage = random.randint(1,3)
        print(f'\nYou deal {damage} damage to the Rat')
        # ---- To implement editing of RatHP - damage properly ----
        if RatHP == 0:
            print("The Rat is dead! You are victorious!")
            main.outdoor_menu()
        else:
            RatHP = RatHP - damage
            main.combat_menu()
    else:
        print("\nYou run and hide.")
        main.outdoor_menu()

# Function for outdoor menu choices
def outdoor_menu_choices(outdoorChoice):
    if outdoorChoice == 1:
        # Enter code for view character
        pass
    # elif outdoorchoice == 2:
        # Enter code for viewing map
    elif outdoorChoice == 3:
        # Enter code for moving + map
        main.combat_menu()
    else:
        # Enter code for exiting game
        pass

main = Menu()
main.main_menu()
