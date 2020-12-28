import pygame

### Classes

## Definiing the 'world'
class World(object):

    def __init__(self):
        self.entities = {}
        self.entity_id = 0

    def add_entity(self,entity):

        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self,entity):

        del self.entities[entity.id]

    def get_id(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None


## Entity objects with id, hp, attack, defense and name values
class GameEntity(object):

    def __init__(self,world,name,attack,defense,hp):

        self.world = world
        self.name = name
        self.id  = 0
        self.attack = attack
        self.defense = defense
        self.hp = hp
