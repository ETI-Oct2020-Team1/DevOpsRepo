import pytest
from ratVentureMenus import combat_menu
from tud_test_base import set_keyboard_input, get_display_output

def test_viewcharacter ():

    set_keyboard_input({1})

    combat_menu()

    output = get_display_output()

    assert output == ["\n1) Attack",
    "2) Run",
    "Enter an option: "]