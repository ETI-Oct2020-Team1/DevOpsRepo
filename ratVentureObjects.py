import pygame
from pynput.keyboard import Key, Listener
import random

### Classes
## Definiing the 'world'
class World(object):

    def __init__(self,rows,layout):
        self.entities = {}
        self.day = 1
        self.map_dict = {0:' - ', 1:  ' H ',2:' T ',3: 'T', 4: ' H/T ', 5:' O ', 6:' K '}
        self.entity_id = 0
        self.rows = rows
        self.layout = layout
        self.tiles = rows * layout
        self.map = []
        for i in range(self.tiles):
            self.map.append(0) 

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
           self.entities[entity_id].hp = hp

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
        #setting it to spawn in tile 3
        self.map_location_id = 3
        self.world.map[self.map_location_id] += 1
        self.orb = False
    def rest(self):
        self.current_hp = self.max_hp
        self.world.add_day()

    #Keyboard detection
    def __on_press(self,key):
        self.__check_key(key)
    def __on_release(self,key):
        if key == Key.esc:
            # Stop listener
            return False
    def __check_key(self,key):
        try:
            if key == Key.up:
                print('Up -8')
                self.world.map[self.map_location_id] -= 1
                self.map_location_id -= 8 
                self.world.map[self.map_location_id] += 1
                self.world.print_map()
            elif key == Key.left: 
                print('left -1')   
                self.world.map[self.map_location_id] -= 1
                self.map_location_id -= 1 
                self.world.map[self.map_location_id] += 1
                self.world.print_map() 
            elif key == Key.down:
                print('down +8')    
                self.world.map[self.map_location_id] -= 1
                self.map_location_id += 8 
                self.world.map[self.map_location_id] += 1
                self.world.print_map()
            # I need to split these up f
            elif key == Key.right:
                print('right +1')
                self.world.map[self.map_location_id] -= 1
                self.map_location_id += 1 
                self.world.map[self.map_location_id] += 1
                self.world.print_map()
            # I need to split these up for some reason cause if I use 'or' statements the arrow keys after the 
            # first statement get ignored and dont even go into the else statement
            else:
                if key.char in ['w','W']: 
                    print('W: Up -8')
                elif key.char in ['a','A']:
                    print('A: left -1') 
                elif key.char in ['s','S']:
                     print('S: down +8')
                elif key.char in ['d','D']:
                    print('D: right +1')
                    if (self.player.map_location_id) >= self.layout:
                        print("you cant go that way")
                    else:
                        self.world.map[self.map_location_id] -= 1
                        self.map_location_id += 1 
                        self.world.map[self.map_location_id] += 1
                        self.world.print_map() 
                else:
                    print("Not a movement command")
        # If something like key.esc or key.space it will just return and loop without throwing an error
        # Attribute error is what occurs so I am only silencing this one as key.esc is the current stop command
        # This is a VERY BAD practice never do this.
        except(AttributeError):
            return
    def move(self):
        self.world.print_map()
        # Collect events until released
        # This is the listener that uses the other functions to check the keys being pressed
        # move() is what calls the listener 
        with Listener( on_press=self.__on_press, on_release=self.__on_release) as listener:
            listener.join()
        return listener.stop()
    
