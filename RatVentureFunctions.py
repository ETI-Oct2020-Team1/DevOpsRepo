from RatVentureObjects import *
import random

def damage(self,target):
    rawDamage = random.randint(self.attack[0],self.attack[1])
    calcDamage = rawDamage - target.defense;
    if calcDamage < 0:
        calcDamage = 0;
    target.hp -= calcDamage;
    print(target.name, "took", calcDamage, "damage!", "\n" + target.name, "now has",target.hp, "hp left!")
    
