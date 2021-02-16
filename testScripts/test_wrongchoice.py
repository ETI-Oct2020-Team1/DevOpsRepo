# import pytest
# import ratVenture
# from unittest import mock
# from ratVentureMenus import *
# from ratVentureFunctions import *
# from tud_test_base import set_keyboard_input, get_display_output



# def mock_input(s):
#     output.append(s)
#     return input_values.pop(0)

# def test_exitgame():
#     input_values = "3"
#     output = [quit()]
#     ratVentureMenus.choice = mock_input
#     ratVenture.print = lambda s : output.append(s)

#     ratVenture.run()

#     assert output == [""] 

# def test_exits():
#     test = False
#     input_values = "3"
#     try: 
#         ratVentureMenus.choice = mock_input
#         ratVenture.print = lambda s : output.append(s)

#         ratVenture.run()
#     except SystemExit as e:
#         if e.code == 0:
#             test = True

#     assert test