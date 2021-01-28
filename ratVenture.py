from ratVentureMenus import * 

def run():
    ### Initialization
    world = World(8,8)
    ### Player must always be initialized first
    player = Player(world, "The Hero",[2,4],1,20)
    rat = GameEntity(world,"The rat",[1,3],1,10)
    
    world.add_entity(player)
    world.add_entity(rat)

    
    ### Game runTime
    while True:
        main_menu(world)


    

while True:
    run()
    

