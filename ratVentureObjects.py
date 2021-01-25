import pygame

### Classes

## Definiing the 'world'
class World(object):

    def __init__(self):
        self.entities = {}
        self.day = 1
        self.map = ['H/T',' - ',' - ',' - ',' - ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' T ',' - ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' - ',' - ',' T ',' - ',' - ',
                    ' T ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' - ',' T ',' - ',' - ',' - ',
                    ' - ',' - ',' - ',' - ',' - ',' - ',' - ',' K ']
        self.entity_id = 0
        self.rows = 0
        self.layout = 0
        self.tiles = 0
        self.map = []
        self.initMap(self.tiles,self.layout)

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

    def initMap(self,rows,layout):
        self.rows = rows
        self.layout = layout
        self.tiles = rows*layout
        for i in range(self.tiles):
            self.map.append(' - ')
        return self.map
        
    def get_map(self):
        return self.map

    def print_map(self):
        counter = 0
        #print("|",end=" ")
        #print(self.tiles)
        counter=0
        for i in self.map:
            if i==self.tiles:
                print()
                break
            if counter == self.layout:
                print("|")
                counter = 0
            print("|",i, end = " ")
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

## Entity objects with id, hp, attack, defense and name values
class GameEntity(object):

    def __init__(self,world,name,attack,defense,hp):

        self.world = world
        self.name = name
        self.id  = 0
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def get_id(self):
        return self.id
    
    #def update_entity(world,entity_id,name,attack,defense,hp):
     #   if World.get(world,entity_id):
      #      world.entities[entity_id].name = name
       #     world.entities[entity_id].attack = attack
        #    world.entities[entity_id].defense = defense
         #   world.entities[entity_id].hp = hp

