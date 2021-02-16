# import pytest
# from ratVentureMenus import *


# world = World(8,8)


# def test_newgame ():

#     # main_menu(world)
#     # input = lambda: "1"

#     def output(input_value):


#         print("Welcome to Ratventure!")
#         print("----------------------")
#         print("1) New Game")
#         print("2) Resume Game")
#         print("3) Exit Game")
#         try:
#             choice = int (input_value)
#             if choice == 1:
#                 main_menu(world).input = choice
#             elif choice == 2:
#                 return
#             elif choice == 3:
#                 return
#             else:
#                 print("Please enter an option from 1-3!")
#                 return main_menu(world)
#         except ValueError:
#             print("Please enter an option from 1-3!")
#             return main_menu(world)


#     assert output("1") == town_menu(world)

# #"1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n 6) Exit Game\nEnter an option: "