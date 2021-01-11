import pytest
from ratVentureMenus import outdoor_menu
from tud_test_base import set_keyboard_input, get_display_output

def test_viewcharacter ():

    set_keyboard_input({1})

    outdoor_menu()

    output = get_display_output()

    assert output == ["1) View Character",
    "2) View Map",
    "3) Move",
    "4) Exit Game",
    "Enter an option: "]