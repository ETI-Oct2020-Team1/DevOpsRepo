from ratVentureObjects import *
import pickle

'''
    Contributors: Zi Hui, Zechariah
    This file consists of menus for the ratVenture program
    as well as the features for saving and loading the game progress,
    and the feature to print the player's statistics.
'''

# UI for Town Menu
def town_menu(world):
    print("\nDay ",world.get_day(),": You are in a town.")
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
            print("Use 'wasd' or arrow keys to choose a direction to move")
            world.get_player().move()
            return combat_menu(world)
        elif choice == 4:
            world.get_player().rest()
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
        print("Value error: Please enter an option from 1-6!\n")
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
            if world.map[world.get_player().map_location_id] in [2,3,4]:
                return town_menu(world)
            elif world.map[world.get_player().map_location_id] == 1 or world.map[world.get_player().map_location_id] == 6:
                if world.get_player().target == None:
                    return outdoor_menu(world)
                else:
                    print(world.get_player().target.name)
                    return combat_menu(world) 
            
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
    print(f"Name:{player.name}")
    print(f"Damage:{player.attack[0]}-{player.attack[1]}")
    print(f"Defense:{player.defense}")
    print(f"Current HP:{player.current_hp}")
    print(f"Max HP:{player.max_hp}")
    print(f"Obtained orb:{player.orb}\n")


# UI for Outdoor Menu
def outdoor_menu(world):
    player = world.get_player()
    if world.map[player.map_location_id] == 3:
        return town_menu(world)
  # print out either the attack or run message
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            player_stats(world)
            return outdoor_menu(world)
        elif choice == 2:
            world.print_map()
            return outdoor_menu(world)
        elif choice == 3:
            world.get_player().move()
            combat_menu(world)
        elif choice == 4:
            return check_exit(world)
        else:
            print("Please enter an option from 1-4!\n")
            return outdoor_menu(world)
    except ValueError:
        print("Please enter an option from 1-4!\n")
        return outdoor_menu(world)


# UI for Combat Menu
def combat_menu(world):
    player = world.get_player() 
    target = player.target
    if world.map[player.map_location_id] not in [2,3,4]:
        if player.target is None: 
            player.combat()
            target = player.target
        #print("Damage: ",target.attack[0],target.attack[2])
        if type(target) == RatKing:
            print("\nDay ", world.get_day() ,": You see the Rat King!")
        else:
            print("\nDay ", world.get_day() ,": You are out in the open.")
        print("Encounter! - {0}\nDamage: {1}-{2}\nDefence: {3}\nHealth: {4}".format(target.name,target.attack[0],target.attack[1],target.defense,target.current_hp))
        print("1) Attack")
        print("2) Run")
        try:
            choice = int(input("Enter an option: "))
            if choice == 1:
                world.get_player().damage(target)
                if world.get_player().target.current_hp <= 0:
                    world.get_player().target = None
                    if world.gameWin():
                        return False
                    else:
                        return outdoor_menu(world) 
                if target.damage(world.get_player()):
                    return False
                else:
                    return combat_menu(world)
            elif choice == 2:
                return run_menu(world,target)
            else:
                print("Please enter an option from 1-2!\n")
                return combat_menu(world)
        except ValueError:
            print("Please enter an option from 1-2!\n")
            return combat_menu(world)
    else:
        return outdoor_menu(world)


# UI for Outdoor Menu
def run_menu(world,target):
    print("\nYou run and hide.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game\n")
    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            target.current_hp = target.max_hp
            player_stats(world)
            print("\nThe enemy patched up their wounds!")
            target.damage(world.get_player())
            return combat_menu(world)
        elif choice == 2:
            target.current_hp = target.max_hp
            world.print_map()
            print("\nThe enemy patched up their wounds!")
            target.damage(world.get_player())
            return combat_menu(world)
        elif choice == 3:
            if world.get_player().target != None:
                        world.get_player().target = None
            world.get_player().move()
            if world.map[world.get_player().map_location_id] == 6:
                return combat_menu(world)
            else:
                return outdoor_menu(world)
        elif choice == 4:
            clarify = input("\nExiting game now will not save combat progress. Proceed with exiting game? Y/N: ")
            if clarify == "Y" or clarify == "y":
                return check_exit(world)
            elif clarify == "N" or clarify == "n":
                return run_menu(world,target)
            else:
                print("\nInvalid option entered.")
                return run_menu(world,target)
        else:
            print("Please enter an option from 1-4!\n")
            return run_menu(world,target)
    except ValueError:
        print("Please enter an option from 1-4!\n")
        return run_menu(world,target)


# Function to save game data
def saveGame(world):
    # Retrieve current world information
    player = world.get_player()
    target = world.get_target()
    load_day = world.get_day()
    map = world.get_map()
    rows = world.get_rows()
    layout = world.get_layout()
    noTown = world.get_noTown()
    entities = world.get_entities()

    pickle_out = open("save.pickle", "wb") # Open a pickle file to write

    # Dump the information retrieved into the pickle file
    pickle.dump(player, pickle_out)
    pickle.dump(target, pickle_out)
    pickle.dump(load_day, pickle_out)
    pickle.dump(map, pickle_out)
    pickle.dump(rows, pickle_out)
    pickle.dump(layout, pickle_out)
    pickle.dump(noTown, pickle_out)
    pickle.dump(entities, pickle_out)

    pickle_out.close() # Close the pickle file


# Function to load game data
def loadGame(world):
    pickle_in = open("save.pickle", "rb") # Open saved pickle file to read

    # Load saved information and update into world
    player = pickle.load(pickle_in) # player information
    player = world.update_entity(player.id,player.name,player.attack,player.defense,player.current_hp,player.orb,player.target)
    target = pickle.load(pickle_in) # target information
    target = world.update_target(target)
    load_day = pickle.load(pickle_in) # day information
    load_day = world.update_day(load_day)
    map = pickle.load(pickle_in) # map information
    map = world.update_map(map)
    rows = pickle.load(pickle_in) # rows information
    rows = world.update_rows(rows)
    layout = pickle.load(pickle_in) # layout information
    layout = world.update_layout(layout)
    noTown = pickle.load(pickle_in) # noTown information
    noTown = world.update_noTown(noTown)
    entities = pickle.load(pickle_in) # entities information
    entities = world.update_entities(entities)
