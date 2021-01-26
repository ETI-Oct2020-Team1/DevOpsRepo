from ratVentureMenus import * 

dayNum = 1 #global variable for the day number



def run():
    ### Initialization
    world = World()
    ### Player must always be initialized first
    player = GameEntity(world, "The Hero",[2,4],1,20)
    rat = GameEntity(world,"The rat",[1,3],1,10)
    
    world.add_entity(player)
    world.add_entity(rat)

    world.initMap(8,8)
    
    main_menu(world)

    ### Game runTime
    while True:
        print("check")
        main_menu(world)


    #print(player.name)
    #print(player.id)
    #print(player.attack)
    #print(player.hp)
    #print(rat.id)
    
    

while True:
    run()
    

