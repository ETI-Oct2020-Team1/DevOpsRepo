import pytest
from ratVentureMenus import main_menu
from ratVentureMenus import town_menu
from tud_test_base import set_keyboard_input, get_display_output

def test_newgame ():

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

