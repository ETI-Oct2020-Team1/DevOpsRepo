import pytest
from ratVentureMenus import town_menu
from tud_test_base import set_keyboard_input, get_display_output

def test_viewcharacter ():

    set_keyboard_input({1})

    town_menu()

    output = get_display_output()

    assert output == ["The Hero:",
                        "Damage:",
                        "Defence:",
                        "HP:"]

def test_viewmap ():

    set_keyboard_input({2})

    town_menu()

    output = get_display_output()

    assert output == []

def test_move ():

    set_keyboard_input({3})

    town_menu()

    output = get_display_output()

    assert output == []

def test_rest ():

    set_keyboard_input({4})

    town_menu()

    output = get_display_output()

    assert output == ["You are fully healed"]

def test_savegame ():

    set_keyboard_input({5})

    town_menu()

    output = get_display_output()

    assert output == []

def test_exitgame ():

    set_keyboard_input({6})

    town_menu()

    output = get_display_output()

    assert output == []
