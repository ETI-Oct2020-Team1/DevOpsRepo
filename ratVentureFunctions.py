from ratVentureObjects import *
import random


def damage(self,target):
    rawDamage = random.randint(self.attack[0],self.attack[1])
    calcDamage = rawDamage - target.defense
    if calcDamage < 0:
        calcDamage = 0
    target.hp -= calcDamage

    if target.hp <= 0:
        if target.name != "The Hero":
            print("The",target.name,"is dead! You are victorious!")
            return True
        else:
            print("Oh no!",target.name,"died! Game over :(\n")
            return True
    else:
        print(target.name, "took", calcDamage, "damage!", "\n" + target.name, "now has",target.hp, "hp left!\n")
    #GameEntity.update_entity(world,target.id,target.name,target.attack,target.defense,target.hp)
    
