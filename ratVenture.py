from ratVentureMenus import * 
import random

dayNum = 1 #global variable for the day number



def run():
    ### Initialization
    world = World()
    ### Player must always be initialized first
    player = GameEntity(world, "The Hero",[1,40],1,20)
    rat = GameEntity(world,"The rat",[0,0],1,20)
    
    world.add_entity(player)
    world.add_entity(rat)

    for i in world.entities:
        print(world.entities[i].name)

    ### Game runTime
    while True:
        #main_menu()
        test = int(input("Input a test option 1-2: "))
        if test == 1:
            combat_menu(player,rat)
        if test == 2:
            player_stats(world,0)

    #print(player.name)
    #print(player.id)
    #print(player.attack)
    #print(player.hp)
    #print(rat.id)
    #main.main_menu()

while True:
    run()

