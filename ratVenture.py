from ratVentureMenus import * 



def run():
    ### Initialization
    world = World(8,8)
    ### Player must always be initialized first
    player = Player(world, "The Hero",[2,4],1,20)
    rat = GameEntity(world,"The Rat",[1,3],1,10)
    orb = powerOrb(world)
    rat_king = GameEntity(world,"The Rat King",[8,12],5,25)
    
    world.add_entity(player)
    world.add_entity(rat)
    world.add_entity(orb)
    
    ### Game runTime
    while True:
        #combat_menu(world,rat)
        main_menu(world)
    

while True:
    run()