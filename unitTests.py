from ratVentureMenus import *
import unittest
from pynput.keyboard import Key, Controller
from mock import patch

####################################################################################
####################################################################################
####################################################################################

#Before running this file make sure to pip install "mock" 

####################################################################################
####################################################################################
####################################################################################

class TestMenu(unittest.TestCase):
    
    # To test the main menu
    def test_mainMenu(self):
        world = World(8,8) #Initialize world

        #List of inputs for the test
        test_cases = [
            "1",
            "3",
            "a",
            "4"
        ]

        #List of return functions for the inputs
        mock_funcs = [
            "ratVentureMenus.town_menu",
            "builtins.quit",
            "ratVentureMenus.main_menu",
            "ratVentureMenus.main_menu"
        ]

        #List of parameters for the functions
        expect_call_withs = [
            [world],
            [],
            [world],
            [world]
        ]

        #Zip the items in the three lists so that the first items in each list will be placed together
        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
            #patch the builtins input with our inputs for mocking
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                main_menu(world)
                mock.assert_called_once_with(*expect_call_with)


    #To test town menu
    def test_townMenu(self):
        world = World(8,8) #initialize world

        #List of inputs for the test
        test_cases = [
            "2",
            "6",
            "d",
            "8"
        ]

        mock_funcs = [
            "ratVentureMenus.town_menu",
            "ratVentureMenus.check_exit",
            "ratVentureMenus.town_menu",
            "ratVentureMenus.town_menu"
        ]

        expect_call_withs = [
            [world],
            [world],
            [world],
            [world]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                town_menu(world)
                mock.assert_called_once_with(*expect_call_with)


    # ------ Test case not working after update of while true: ------
    # To test combat menu
    # def test_combatMenu(self):

    #     def worldSetup(map_id):
    #         world = World(8,8)
    #         player = Player(world, "The Hero",[1,5],1,20)
    #         rat = GameEntity(world,"The rat",[1,3],1,20)
    #         world.add_entity(player)
    #         world.add_entity(rat)
    #         # target = world.get_player().target
    #         if map_id is not None:
    #             world.map[player.map_location_id] = map_id
    #         return world
                
    #     worlds = [worldSetup(i) for i in [1,5,6,0,2,None]]
    #     target = None

    #     #List of inputs for the test
    #     test_cases = [
    #         "1",
    #         "2",
    #         "c",
    #         "10",
    #         "",
    #         ""
    #     ]

    #     mock_funcs = [
    #         "ratVentureMenus.combat_menu",
    #         "ratVentureMenus.run_menu",
    #         "ratVentureMenus.combat_menu",
    #         "ratVentureMenus.combat_menu",
    #         "ratVentureMenus.outdoor_menu",
    #         "ratVentureMenus.outdoor_menu"
    #     ]

    #     expect_call_withs = [
    #         [worlds[0]],
    #         [worlds[1],target],
    #         [worlds[2]],
    #         [worlds[3]],
    #         [worlds[4]],
    #         [worlds[5]]
    #     ]

    #     for world, test_case, mock_func, expect_call_with in zip(worlds, test_cases, mock_funcs, expect_call_withs):
    #         print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
    #         with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
    #             combat_menu(world)
    #             mock.assert_called_once_with(*expect_call_with)


    # ------ To run test, comment out lines 109-111 in ratVentureMenu.py------
    # To test outdoor menu
    # def test_outdoorMenu(self):
    #     world = World(8,8)
    #     player = Player(world, "The Hero",[1,5],1,20)
    #     rat = GameEntity(world,"The rat",[1,3],1,20)
    #     world.add_entity(player)
    #     world.add_entity(rat)

    #     List of inputs for the test
    #     test_cases = [
    #         "1",
    #         "4",
    #         "f",
    #         "9"
    #     ]

    #     mock_funcs = [
    #         "ratVentureMenus.outdoor_menu",
    #         "ratVentureMenus.check_exit",
    #         "ratVentureMenus.outdoor_menu",
    #         "ratVentureMenus.outdoor_menu"
    #     ]

    #     expect_call_withs = [
    #         [world],
    #         [world],
    #         [world],
    #         [world]
    #     ]

    #     for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
    #         print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
    #         with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
    #             outdoor_menu(world)
    #             mock.assert_called_once_with(*expect_call_with)

    
    # To test run menu
    def test_runMenu(self):
        world = World(8,8)
        player = Player(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)
        target = rat

        test_cases = [
            "1",
            "2",
            "h",
            "7"
        ]

        mock_funcs = [
            "ratVentureMenus.combat_menu",
            "ratVentureMenus.combat_menu",
            "ratVentureMenus.run_menu",
            "ratVentureMenus.run_menu"
        ]

        expect_call_withs = [
            [world],
            [world],
            [world,target],
            [world,target]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                run_menu(world,target)
                mock.assert_called_once_with(*expect_call_with)


    # To test checks before exiting menu
    def test_checkSavingBeforeExit(self):
        world = World(8,8)
        player = Player(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)

        test_cases = [
            "Y",
            "n",
            "q",
            "1"
        ]

        mock_funcs = [
            "builtins.quit",
            "builtins.quit",
            "ratVentureMenus.town_menu",
            "ratVentureMenus.town_menu"
        ]

        expect_call_withs = [
            [],
            [],
            [world],
            [world]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                check_exit(world)
                mock.assert_called_once_with(*expect_call_with)


    # To test player stats menu
    def test_playerStats(self):
        world = World(8,8)
        player = Player(world, "The Hero",[1,5],1,20)
        world.add_entity(player)
        player = world.get(0)

        with patch("builtins.print") as mock:
            player_stats(world)

        print_args = mock.call_args_list
        expected_strs = [
            "Name:The Hero",
            "Damage:1-5",
            "Defense:1",
            "Current HP:20",
            "Max HP:20",
            "Obtained orb:False\n"
        ]

        for print_arg, expected_str in zip (print_args,expected_strs):
            print(f"passed into print(): {print_arg.args[0]}, expected: {expected_str}")
            self.assertEqual(print_arg.args[0],expected_str)


if __name__ == "__main__":
    unittest.main(exit=False)  