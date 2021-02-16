from ratVentureMenus import * 

status = True #changed variable was created to control the while loop inside ratVentureMenus.
pytest = False #changed variable was created to check if pytest was running. 

### Initialization
world = World(8,8)
### Player must always be initialized first
player = Player(world, "The Hero",[2,4],1,20)
rat = GameEntity(world,"The Rat",[1,3],1,10)
orb = powerOrb(world)
rat_king = RatKing(world,"The Rat King",[8,12],5,25)

world.add_entity(player)
world.add_entity(rat)
world.add_entity(orb)
world.add_entity(rat_king)
vicText = "You have slain the rat king! The kingdom is saved!"
defText = "  You died  "
### Game runTime
while status:
    main_menu(world)
    
    if world.gameWin():
        print("=" * len(vicText))
        print(vicText)
        print("=" * len(vicText))
        break
    elif world.get_player().current_hp<=0:
        print("=" * len(defText))
        print(defText)
        print("=" * len(defText))
        break
