import pygame

### Classes

## Definiing the 'world'
class World(object):

    def __init__(self):
        self.entities = {}
        self.day = 0
        self.map = {'T','','','','','','','',
                    '','','','T','','','','',
                    '','','','','','T','','',
                    'T','','','','','','','',
                    '','','','','','','','',
                    '','','','','','','','',
                    '','','','','T','','','',
                    '','','','','','','','K',}
        self.entity_id = 0

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

    #def update_entity(self,entity_id,name,attack,defense,hp):
     #   if self.get(self,entity_id):
      #      entities[entity_id].name = name
       #     entities[entity_id].attack = attack
        #    entities[entity_id].defense = defense
         #   entities[entity_id].hp = hp


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

