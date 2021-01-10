from ratVentureFunctions import *
import pickle

# UI for Town Menu
def town_menu(world):
    #print("\nDay ",dayNum,": You are in a town.")
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
            world.get_map()
            return town_menu(world)
        elif choice == 3:
            world.get_map()
            move()
            return town_menu(world)
        elif choice == 4:
            return
        elif choice == 5:
            saveGame(world)
        elif choice == 6:
            return quit()
        else:
            print("Please enter an option from 1-6!\n")
            return town_menu(world)
    except ValueError:
        print("Please enter an option from 1-6!\n")
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
            return
        elif choice == 3:
            return quit()
        else:
            print("Please enter an option from 1-3!\n")
            return main_menu(world)
    except ValueError:
        print("Please enter an option from 1-3!\n")
        return main_menu(world)

def player_stats(world):
    player = world.get(0)
    #player = World.get(World,entity_id)
    print("Name:",player.name)
    print("Damage:", player.attack[0],"-",player.attack[1])
    print("Defense:",player.defense)
    print("Current HP:",player.hp,"\n")
    return town_menu(world)

#UI for Outdoor Menu
def outdoor_menu(world,attacker,defender):
  # print out either the attack or run message
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game\n")

    try:
        choice = int(input("Enter an option: "))
        if choice == 1:
            return player_stats(world)
        elif choice == 2:
            move()
            return outdoor_menu(world,attacker,defender)
        elif choice == 3:
            return
        elif choice == 4:
            return quit()
        elif choice == 5:
            return combat_menu(world,attacker,defender)
        else:
            print("Please enter an option from 1-4!\n")
            return outdoor_menu(world,attacker,defender)
    except ValueError:
        print("Please enter an option from 1-4!\n")
        return outdoor_menu(world,attacker,defender)

#UI for Combat Menu
def combat_menu(world,attacker,defender):
    #print("\nDay ",dayNum,": You are out in the open.")
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
            return outdoor_menu(world,attacker,defender)
        else:
            print("Please enter an option from 1-2!\n")
            return combat_menu(world,attacker,defender)
    except ValueError:
        print("Please enter an option from 1-2!\n")
        return 

        print("Please enter an option from 1-2!")
        return 

def saveGame(world):
    player = world.get(0)
    pickle_out = open("save.pickle", "wb")
    pickle.dump(player, pickle_out)
    pickle_out.close()

def loadGame(world):
    pickle_in = open("save.pickle", "rb")
    player = pickle.load(pickle_in)
    player = world.update_entity(player.id,player.name,player.attack,player.defense,player.hp)
