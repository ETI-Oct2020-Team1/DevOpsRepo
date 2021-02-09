import pygame
from pynput.keyboard import Key, Listener
import random

### Classes
## Definiing the 'world'
class World(object):

    def __init__(self,rows,layout):
        self.entities = {}
        self.day = 1
        self.map_dict = {0:' - ', 1: ' H ',2:' T ',3: 'H/T', 4:'O/T', 5:' K ', 6: 'H/K'}
        self.entity_id = 0
        self.rows = rows
        self.layout = layout
        self.tiles = rows * layout
        self.map = []
        self.noTown = layout/2
        self.townLocations = [0]    #Starting town
        for town in range(int(self.noTown)-1): #-1 cause starting town is always 0
            town = random.randint(1,self.tiles-1)
            if town in self.townLocations:
                town = random.randint(1,self.tiles-1)   #If duplicate number
            self.townLocations.append(town)
        for i in range(self.tiles):
            self.map.append(0) 
            if i in self.townLocations:
                self.map[i] = 2#Key2:' T '               

    def add_entity(self,entity):

        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self,entity):
        del self.entities[entity.id]    

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def add_day(self):
        self.day += 1

    def get_day(self):
        return self.day

    def get_map(self):
        return self.map

    def print_map(self):
        counter=0
        for i in self.map:
            if i==self.tiles:
                print()
                break
            if counter == self.layout:
                print("|")
                counter = 0
            print("|",self.map_dict.get(i), end = " ")
            counter += 1
        print("|\n")

    def update_entity(self,entity_id,name,attack,defense,hp):
       if self.get(entity_id):
           self.entities[entity_id].name = name
           self.entities[entity_id].attack = attack
           self.entities[entity_id].defense = defense
           self.entities[entity_id].current_hp = hp

    def update_day(self,day):
        self.day = day

    def update_map(self,map):
        self.map = map

    def get_player(self):
        for i in self.entities:
            if self.entities[i].name == "The Hero":
                return self.entities[i]

## Entity objects with id, hp, attack, defense and name values
class GameEntity(object):

    def __init__(self,world,name,attack,defense,hp):

        self.world = world
        self.name = name
        self.id  = 0
        self.attack = attack
        self.defense = defense
        self.max_hp = hp
        self.current_hp = hp

    def get_id(self):
        return self.id
    #def update_entity(world,entity_id,name,attack,defense,hp):
     #   if World.get(world,entity_id):
      #      world.entities[entity_id].name = name
       #     world.entities[entity_id].attack = attack
        #    world.entities[entity_id].defense = defense
         #   world.entities[entity_id].hp = hp
    def damage(self,target):
        rawDamage = random.randint(self.attack[0],self.attack[1])
        calcDamage = rawDamage - target.defense
        if calcDamage < 0:
            calcDamage = 0
        target.current_hp -= calcDamage
        if target.current_hp <= 0:
            if target.name != "The Hero":
                print("The",target.name,"is dead! You are victorious!")
                self.world.add_day()
                return True
            else:
                print("Oh no!",target.name,"died! Game over :(\n")
                return True
        else:
            print(target.name, "took", calcDamage, "damage!", "\n" + target.name, "now has",target.current_hp, "hp left!\n")
    #GameEntity.update_entity(world,target.id,target.name,target.attack,target.defense,target.hp)


class Player(GameEntity):
    def __init__(self,world,name,attack,defense,hp):
        super().__init__(world,name,attack,defense,hp)
        #setting it to spawn in tile 0, the top left of the map
        self.map_location_id = 0
        self.world.map[self.map_location_id] += 1
        self.orb = False

    def rest(self):
        self.current_hp = self.max_hp
        self.world.add_day()

    def __on_press(self,key):
        self.__check_key(key)
        #Comment out this line if you want to do consecutive movement testing
        #return False
    def __on_release(self,key):
        if key == Key.esc:
            # Stop listener
            return False
    def __check_key(self,key):
        try:
            if key == Key.up:
                self.move_up()
            elif key == Key.left:  
                self.move_left() 
            elif key == Key.down:
                self.move_down()
            elif key == Key.right:
                self.move_right()
            # I need to split these up for some reason cause if I use 'or' statements the arrow keys after the 
            # first statement get ignored and dont even go into the else statement
            else:
                if key.char in ['w','W']: 
                    self.move_up()
                elif key.char in ['a','A']:
                    self.move_left() 
                elif key.char in ['s','S']:
                    self.move_down()
                elif key.char in ['d','D']:
                    self.move_up() 
                else:
                    print("Not a movement command")           
        # If something like key.esc or key.space it will just return and loop without throwing an error
        # Attribute error is what occurs so I am only silencing this one as key.esc is the current stop command
        # This is a VERY BAD practice never do this.
        except(AttributeError):
            return
        #self.checkTile()
    #   Maps and stuff will call this function which activates the listener, within the listeners check_keys
    #   the actual movement functions are called 
    def move(self):
        # Pynput: Collect events until released
        # Pynput: This is the listener that uses the other functions to check the keys being pressed 
        self.world.print_map()
        self.world.add_day()
        with Listener( on_press=self.__on_press, on_release=self.__on_release) as listener:
            listener.join()
        return listener.stop()
    
    def move_right(self):
        # + 1 cause the firs row is 0
        if (self.map_location_id + 1) % self.world.layout == 0:
            print("Woah there pal you cant go that way!")
        else:
            # -1 from the item so when printMap() is called it is update to be (for example) 0 if the tile is empty
            self.checkTile(1)
    def move_left(self):
        if (self.map_location_id - 1)  < 0 or  (self.map_location_id) % self.world.layout == 0:
            print("Woah there pal you cant go that way!")
        else:
            self.checkTile(-1)
    
    # For moving up and down you will notice I used
    # self.map_location_id += self.world.layout
    # This makes it so that it will just add the layout number to the 
    # position to make it move directly 'up' or 'down'
    def move_down(self):
        if self.map_location_id + self.world.layout > self.world.tiles - 1:
            print("Woah pal you cant go that way")
        else:  
            self.checkTile(self.world.layout)   
    def move_up(self):
        if self.map_location_id - self.world.layout < 0:
            print("Woah pal you cant go that way")
        else:
            self.checkTile(-self.world.layout)
    #Called in check_key
    def checkTile(self,mVal):
            self.world.add_day()
            self.world.map[self.map_location_id] -= 1
            # If tile is an 'O/T' tile...
            ##self.world.map[self.map_location_id] - 1
            if self.world.map[ self.map_location_id + mVal] == 4:
                self.map_location_id += mVal
                self.world.map[self.map_location_id] = 3
                powerOrb.power(self,self)
                self.world.print_map()
                return True
            else:
                self.map_location_id += mVal 
                self.world.map[self.map_location_id] += 1
                self.world.print_map()
                return True
            

class powerOrb(GameEntity):
    def __init__(self,world):
        self.name = "Orb of Power"
        self.world = world
        # Picking a random town from the townLocations list[1-max]
        # It will never spawn in the first town
        self.map_location_id = self.world.townLocations[random.randint(1,len(self.world.townLocations)-1)]
        self.world.map[self.map_location_id] = 4 #Key4: 'O/T'

    def power(self,player):
        if player.name == "The Hero" and player.orb == False:
            player.attack = [x + 5 for x in player.attack]
            player.defense += 5
            player.orb = True
