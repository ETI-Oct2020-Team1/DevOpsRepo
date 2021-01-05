from ratVentureObjects import *
from pynput.keyboard import Key, Listener
import random

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    if key in [Key.up, Key.down, Key.left, Key.right]: 
        print('YES')

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
    
def move():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    
    
    
    