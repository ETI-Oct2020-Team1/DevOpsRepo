from ratVentureObjects import *
from pynput.keyboard import Key, Listener
import random

def on_press(key):
    check_key(key)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    #checking for movement options
    try:
        #print("Check: ",key)
        #WASD movement works but arrow keys stop at the first if statement
        if key == Key.up:
            print('Up +8')
        elif key == Key.left: 
            print('left -1')    
        elif key == Key.down:
            print('down -8')
        elif key == Key.right: 
            print('right +1')  
        # I need to split these up for some reason cause if I use 'or' statements the arrow keys after the 
        # first statement get ignored and dont even go into the else statement
        else:
            if key.char in ['w','W']: 
                print('Up +8')
            elif key.char in ['a','A']:
                print('left -1') 
            elif key.char in ['s','S']:
                 print('down -8')
            elif key.char in ['d','D']:
                print('right +1') 
            else:
                print("Not a movement command")
    # If something like key.esc or key.space it will just return and loop without throwing an error
    # Attribute error is what occurs so I am only silencing this one as key.esc is the current stop command
    # This is a VERY BAD practice never do this.
    except(AttributeError):
        return

def damage(attacker,target):
    rawDamage = random.randint(attacker.attack[0],attacker.attack[1])
    calcDamage = rawDamage - target.defense
    if calcDamage < 0:
        calcDamage = 0
    target.current_hp -= calcDamage

    if target.current_hp <= 0:
        if target.name != "The Hero":
            print("The",target.name,"is dead! You are victorious!")
            return True
        else:
            print("Oh no!",target.name,"died! Game over :(\n")
            return True
    else:
        print(target.name, "took", calcDamage, "damage!", "\n" + target.name, "now has",target.current_hp, "hp left!\n")
    