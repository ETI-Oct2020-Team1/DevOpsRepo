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
        print(key)
        #WASD movement works but arrow keys stop at the first if statement
        if key == Key.up or key.char in ['w','W']: 
            print('Up +8')
            #Keyboard.press(Key.esc)
        elif key == Key.left or key.char in ['a','A']: 
            print('left -1')    
        elif key == Key.down or key.char in ['s','S']: 
            print('down -8')
        elif key == Key.right or key.char in ['d','D']: 
            print('right +1')  
        else:
            print("Not a movement command")
    # If something like key.esc or key.space it will just return and loop without throwing an error
    # Attribute error is what occurs so I am only silencing this one as key.esc is the current stop command
    # This is a VERY BAD practice never do this.
    except(AttributeError):
        return

def move():
    # Collect events until released
    # This is the listener that uses the other functions to check the keys being pressed
    # move() is what calls the listener 
    with Listener( on_press=on_press, on_release=on_release) as listener:
        listener.join()
    return listener.stop()

def damage(attacker,target):
    rawDamage = random.randint(attacker.attack[0],attacker.attack[1])
    calcDamage = rawDamage - target.defense
    if calcDamage < 0:
        calcDamage = 0
    target.current_hp -= calcDamage

    if target.current_hp <= 0:
        if target.name != "The Hero":
            print("The",target.name,"is dead! You are victorious!")
            attacker.world.add_day()
            return True
        else:
            print("Oh no!",target.name,"died! Game over :(\n")
            return True
    else:
        print(target.name, "took", calcDamage, "damage!", "\n" + target.name, "now has",target.current_hp, "hp left!\n")
    #GameEntity.update_entity(world,target.id,target.name,target.attack,target.defense,target.hp)

def rest(world):
    for i in world.entities:
        if world.entities[i].name == "The Hero":
            world.entities[i].current_hp = world.entities[i].max_hp
    world.add_day()
    