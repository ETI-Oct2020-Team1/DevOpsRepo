# Defining the Menus

choice = 0 #global variable for main_menu choices 
townChoice = 0 #global variable for town_menu choices 
combatChoice = 0 #global variable for combat_menu choices
outdoorChoice = 0 #global variable for outdoor_menu choices
dayNum = 1 #global variable for the day number

RatHP = 10 #global variable for the Rat's HP <-- to implement in object file

#To implement this in object file
def rat_object():
    global RatHP
    print("Encounter! - Rat")
    print("Damage: 1-3")
    print("Defence: 1")
    print(f'HP: {RatHP}')


class Menu:
    #UI for Outdoor Menu
    def outdoor_menu(self):
        # print out either the attack or run message
        print("1) View Character")
        print("2) View Map")
        print("3) Move")
        print("4) Exit Game")
        global outdoorChoice
        while 1 > outdoorChoice or 4 < outdoorChoice:
            try:
                outdoorChoice = int(input("Enter choice: "))
                #print(f'Choice is {outdoorChoice}')
            except ValueError:
                print("\nPlease input a number between 1-4.")
        return outdoorChoice

    #UI for Combat Menu
    def combat_menu(self):
        print("\nDay ",dayNum,": You are out in the open.")
        rat_object()
        print("1) Attack")
        print("2) Run")
        global combatChoice
        while 1 > combatChoice or 2 < combatChoice:
            try:
                combatChoice = int(input("Enter choice: "))
                #print(f'Choice is {combatChoice}')
            except ValueError:
                print("\nPlease input a number between 1-2.")
        return combatChoice

    # UI for Town Menu
    def town_menu(self):
        print("\nDay ",dayNum,": You are in a town.")
        print("1) View Character")
        print("2) View Map")
        print("3) Move")
        print("4) Rest")
        print("5) Save Game")
        print("6) Exit Game")
        global townChoice
        while 1 > townChoice or 6 < townChoice:
            try:
                townChoice = int(input("Enter choice: "))
                #print(f'Choice is {townChoice}')
            except ValueError:
                print("\nPlease input a number between 1-6.")
        return townChoice


    # UI for Main Menu
    def main_menu(self):
        print("Welcome to Ratventure!")
        print("----------------------")
        print("1) New Game")
        print("2) Resume Game")
        print("3) Exit Game")
        global choice
        while 1 > choice or 3 < choice:
            try:
                choice = int(input("Enter choice: "))
                #print(f'Choice is {choice}')
            except ValueError:
                print("\nPlease input a number between 1-3.")
        return choice