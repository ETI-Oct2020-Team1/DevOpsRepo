import pytest
from ratVentureMenus import *


world = World()

def test_newgames ():

    # main_menu(world)
    # input = lambda: "1"

    def output():
        return "Welcome to Ratventure!\n ----------------------\n1) New Game\n2) Resume Game \n3) Exit Game \nEnter an option: \n"


    assert output() == "Welcome to Ratventure!\n ----------------------\n1) New Game\n2) Resume Game \n3) Exit Game \nEnter an option: \n"

#"1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n 6) Exit Game\nEnter an option: "