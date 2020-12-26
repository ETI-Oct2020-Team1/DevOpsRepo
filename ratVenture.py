from RatVentureFunctions import * 
#ratVenture.py
#test1

choice = 0 #global variable for main_menu choices 
townChoice = 0 #global variable for town_menu choices 
dayNum = 1 #global variable for the day number

# UI for Town Menu
def town_menu():
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
            town_menu()
    #To implement linking with the other features
    return townChoice

# UI for Main Menu
def main_menu():
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
            main_menu()
    if choice == 1:
        town_menu()
    # elif choice == 2:
        #Enter code for resume game
    # else:
        #Enter code for Exit Game
    return choice

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
