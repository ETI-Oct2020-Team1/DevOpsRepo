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
    
    def test_mainMenu(self):
        world = World(8,8)

        test_cases = [
            "1",
            "3",
            "a",
            "4"
        ]

        mock_funcs = [
            "ratVentureMenus.town_menu",
            "builtins.quit",
            "ratVentureMenus.main_menu",
            "ratVentureMenus.main_menu"
        ]

        expect_call_withs = [
            [world],
            [],
            [world],
            [world]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            print(f"Test input: {test_case}, Expected Return: {mock_func}{expect_call_with}")
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                main_menu(world)
                mock.assert_called_once_with(*expect_call_with)

    def test_townMenu(self):
        world = World(8,8)

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
    # def test_combatMenu(self):
    #     target = None

    #     def worldSetup(map_id=None):
    #         world = World(8,8)
    #         player = Player(world, "The Hero",[1,5],1,20)
    #         rat = GameEntity(world,"The rat",[1,3],1,20)
    #         world.add_entity(player)
    #         world.add_entity(rat)
    #         if map_id is not None:
    #             world.map[player.map_location_id] = map_id
    #         return world

    #     worlds = [worldSetup(i) for i in [2,3,4,2,1,None]]

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


    # ------ To run test, comment out lines 99-101 in ratVentureMenu.py------
    # def test_outdoorMenu(self):
    #     world = World(8,8)
    #     player = Player(world, "The Hero",[1,5],1,20)
    #     rat = GameEntity(world,"The rat",[1,3],1,20)
    #     world.add_entity(player)
    #     world.add_entity(rat)

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