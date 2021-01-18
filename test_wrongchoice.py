import pytest
from ratVentureMenus import *
from ratVentureFunctions import *
from tud_test_base import set_keyboard_input, get_display_output

def test_wrongchoice ():

    set_keyboard_input({4})

    main_menu(World)

    output = get_display_output()

    assert output == ["Welcome to Ratventure!",
    "----------------------",
    "1) New Game",
    "2) Resume Game",
    "3) Exit Game",
    "Enter an option: "]