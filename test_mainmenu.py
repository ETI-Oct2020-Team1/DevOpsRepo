import pytest
from ratVenture import *
from ratVentureMenus import *
from tud_test_base import set_keyboard_input, get_display_output

world = World()

def test_newgame ():

    input_values = "1"
    output = []
 
    def mock_input(s):
        output.append(s)
        return input_values
    ratVenture.input = mock_input
    ratVenture.print = lambda s : output.append(s)

    town_menu(world)

    assert output == ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

def test_one ():

    main_menu()

    output = get_display_output()

    assert output == ["New Game",\
             "Resume Game ",\
             "Exit Game",\
             "Enter an option: "]

def test_exitgame ():

    set_keyboard_input({1})

    main_menu()

    output = get_display_output()

    assert output == ["Day  1 : You are in a town.",\
             "1) View Character",\
             "2) View Map",\
             "3) Move",\
             "4) Rest",\
             "5) Save Game",\
             "6) Exit Game",\
             "Enter an option: s"]

def test_newgame2 ():

    set_keyboard_input({1})

    town_menu

    output = get_display_output()

    assert output == ["Day 1: You are in a town.",
    "1)   View Character",
    "2)   View Map",
    "3)   Move",
    "4)   Rest",
    "5)   Save Game",
    "6)   Exit Game",
    "Enter choice: "]

def test_resumegame ():

    set_keyboard_input({2})

    main_menu

    output = get_display_output()

    assert output == [""]

def test_exitgame ():

    set_keyboard_input({3})

    main_menu

    output = get_display_output()

    assert output == [""]

def test_wrongchoice ():

    set_keyboard_input({4})

    main_menu

    output = get_display_output()

    assert output == ["Welcome to Ratventure!",
    "----------------------",
    "1)   New Game",
    "2)   Resume Game",
    "3)   Exit Game",
    "Enter Choice:",
    "\nPlease input a number between 1-3."]






#"Welcome to Ratventure!", 
#    "----------------------", 
#    "1)   New Game",
#    "2)   Resume Game",
#    "3)   Exit Game",
#    "Enter Choice:"

