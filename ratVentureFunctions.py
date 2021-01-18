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
    #checking for movement options
    try:
        if key in [Key.up] or key.char in ['w']: 
            print('Up +8')
        if key in [Key.left] or key.char in ['a']: 
            print('left -1')    
        if key in [Key.down] or key.char in ['s']: 
            print('down -8')
        if key in [Key.right,] or key.char in ['d']: 
            print('right +1')  
        else:
            print("Not a movement command")
    # If something like key.esc or key.space it will just return and loop without throwing an error
    # Attribute error is what occurs so I am only silencing this one as key.esc is the current stop command
    except(AttributeError):
        return

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
    # This is the listener that uses the other functions to check the keys being pressed
    # move() is what calls the listener 
    with Listener( on_press=on_press, on_release=on_release) as listener:
        listener.join()
    return listener.stop()
    
    
    
    