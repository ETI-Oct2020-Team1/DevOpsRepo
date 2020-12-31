from ratVentureFunctions import *
    
#UI for Outdoor Menu
def outdoor_menu():
  # print out either the attack or run message
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game")

    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            return 
        elif choice == 2:
            return
        elif choice == 3:
            return
        elif choice == 4:
            return
        else:
            print("Please enter an option from 1-4!")
            return outdoor_menu()
    except ValueError:
        print("Please enter an option from 1-4!")
        return outdoor_menu()

#UI for Combat Menu
def combat_menu(player,enemy):
    #print("\nDay ",dayNum,": You are out in the open.")
    print("\n1) Attack")
    print("2) Run")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            
            if damage(player,enemy):
                return main_menu()
            else:
                return combat_menu(player,enemy)
        elif choice == 2:
            return
        else:
            print("Please enter an option from 1-2!")
            return combat_menu(player,enemy)
    except ValueError:
        print("Please enter an option from 1-2!")
        return 

# UI for Town Menu
def town_menu():
    print("\nDay ",dayNum,": You are in a town.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Rest")
    print("5) Save Game")
    print("6) Exit Game")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            return 
        elif choice == 2:
            return
        elif choice == 3:
            return
        elif choice == 4:
            return
        elif choice == 5:
            return
        elif choice == 6:
            return
        else:
            print("Please enter an option from 1-6!")
            return town_menu()
    except ValueError:
        print("Please enter an option from 1-6!")
        return town_menu()

# UI for Main Menu
def main_menu():
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            return 
        elif choice == 2:
            return
        elif choice == 3:
            return
        else:
            print("Please enter an option from 1-3!")
            return main_menu()
    except ValueError:
        print("Please enter an option from 1-3!")
        return main_menu()

#def character_menu():
    #
