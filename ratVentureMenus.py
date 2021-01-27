from ratVentureFunctions import *
import pickle

# UI for Town Menu
def town_menu(world):

    print("\nDay ", world.get_day(),": You are in a town.")

    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Rest")
    print("5) Save Game")
    print("6) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            player_stats(world)
            return town_menu(world)
        elif choice == 2:
            world.print_map()
            return town_menu(world)
        elif choice == 3:
            #world.get_map()
            print("Use 'wasd' or arrow keys to choose a direction to move")

            world.print_map()

            move(world)
            return town_menu(world)
        elif choice == 4:
            rest(world)
            return town_menu(world)
        elif choice == 5:
            saveGame(world)
            print("\nGame saved.")
            return town_menu(world)
        elif choice == 6:
            return check_exit(world)
        else:
            print("Please enter an option from 1-6!\n")
            return town_menu(world)
    except ValueError:
        print("Please enter an option from 1-6!\n")
        return town_menu(world)


# Function to check if user wants to save before exiting game
def check_exit(world):
    clarify = input("\nWould you like to save the game before exiting? Y/N: ")
    if clarify == "Y" or clarify == "y":
        saveGame(world)
        print("\nGame saved.")
        return quit()
    elif clarify == "N" or clarify == "n":
        return quit()
    else:
        print("\nInvalid option entered.")
        return town_menu(world)


# UI for Main Menu
def main_menu(world):
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            return town_menu(world)
        elif choice == 2:
            loadGame(world)
            return town_menu(world)
        elif choice == 3:
            return quit()
        else:
            print("Please enter an option from 1-3!\n")
            return main_menu(world)
    except ValueError:
        print("Please enter an option from 1-3!\n")
        return main_menu(world)


# Function for player statistics
def player_stats(world):
    player = world.get(0)
    #player = World.get(World,entity_id)
    print("Name:",player.name)
    print("Damage:", player.attack[0],"-",player.attack[1])
    print("Defense:",player.defense)
    print("Current HP:",player.current_hp)
    print("Max HP:",player.max_hp,"\n")


# UI for Outdoor Menu
def outdoor_menu(world,attacker,defender):
  # print out either the attack or run message
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            player_stats(world)
            return outdoor_menu(world,attacker,defender)
        elif choice == 2:
            world.print_map()
            return outdoor_menu(world,attacker,defender)
        elif choice == 3:
            world.print_map()
            move()
            return outdoor_menu(world,attacker,defender)
        elif choice == 4:
            return quit()
        else:
            print("Please enter an option from 1-4!\n")
            return outdoor_menu(world,attacker,defender)
    except ValueError:
        print("Please enter an option from 1-4!\n")
        return outdoor_menu(world,attacker,defender)


# UI for Combat Menu
def combat_menu(world,attacker,defender):
    print("\nDay ", world.get_day() ,": You are out in the open.")
    print("1) Attack")
    print("2) Run")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            if damage(attacker,defender):
                return main_menu(world)
            elif damage(defender,attacker):
                return main_menu(world)
            else:
                return combat_menu(world,attacker,defender)
        elif choice == 2:
            return run_menu(world,attacker,defender)
        else:
            print("Please enter an option from 1-2!\n")
            return combat_menu(world,attacker,defender)
    except ValueError:
        print("Please enter an option from 1-2!\n")
        return combat_menu(world,attacker,defender)


# UI for Outdoor Menu
def run_menu(world,attacker,defender):
    print("\nYou run and hide.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            rat = world.get(1)
            rat.hp = 10
            player_stats(world)
            return combat_menu(world,attacker,defender)
        elif choice == 2:
            rat = world.get(1)
            rat.hp = 10
            world.print_map()
            return combat_menu(world,attacker,defender)
        elif choice == 3:
            world.print_map()
            move()
            return outdoor_menu(world,attacker,defender)
        elif choice == 4:
            return quit()
        else:
            print("Please enter an option from 1-4!\n")
            return run_menu(world,attacker,defender)
    except ValueError:
        print("Please enter an option from 1-4!\n")
        return run_menu(world,attacker,defender)


# Function to save game data
def saveGame(world):
    player = world.get(0)
    load_day = world.get_day()
    map = world.get_map()
    pickle_out = open("save.pickle", "wb")
    pickle.dump(player, pickle_out)
    pickle.dump(load_day, pickle_out)
    pickle.dump(map, pickle_out)
    pickle_out.close()

# Function to load game data
def loadGame(world):
    pickle_in = open("save.pickle", "rb")
    player = pickle.load(pickle_in)
    player = world.update_entity(player.id,player.name,player.attack,player.defense,player.hp)
    load_day = pickle.load(pickle_in)
    load_day = world.update_day(load_day)
    map = pickle.load(pickle_in)
    map = world.update_map(map)
