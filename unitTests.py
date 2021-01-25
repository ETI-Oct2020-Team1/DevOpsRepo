from ratVentureMenus import *
import unittest
from mock import patch

#####################################################################################
#####################################################################################
#####################################################################################
#
# Before running this file make sure to pip install "mock" 
#
#####################################################################################
#####################################################################################
#####################################################################################

class TestMenu(unittest.TestCase):
    
    # def test_mainMenu_correctOptionTownMenu(self):
    #     world = World()
    #     with patch('builtins.input', return_value="1"), patch('ratVentureMenus.town_menu') as townMenuMock:
    #         main_menu(world)
    #         townMenuMock.assert_called_once_with(world)
    
    # def test_mainMenu_correctOptionQuit(self):
    #     world = World()
    #     with patch('builtins.input', return_value="3"), patch('builtins.quit') as quitMock:
    #         main_menu(world)
    #         quitMock.assert_called_once_with()

    # def test_mainMenu_nonInteger(self):
    #     world = World()
    #     with patch('builtins.input', return_value="a"), patch('ratVentureMenus.main_menu') as mainMenuMock:
    #         main_menu(world)
    #         mainMenuMock.assert_called_once_with(world)

    # def test_mainMenu_outOfBounds(self):
    #     world = World()
    #     with patch('builtins.input', return_value="4"), patch('ratVentureMenus.main_menu') as mainMenuMock:
    #         main_menu(world)
    #         mainMenuMock.assert_called_once_with(world)  
    
    def test_mainMenu(self):
        world = World()

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
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                main_menu(world)
                mock.assert_called_once_with(*expect_call_with)



    def test_townMenu(self):
        world = World()

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
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                town_menu(world)
                mock.assert_called_once_with(*expect_call_with)



    def test_combatMenu(self):
        world = World()
        player = GameEntity(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)

        test_cases = [
            "1",
            "2",
            "c",
            "10"
        ]

        mock_funcs = [
            "ratVentureMenus.combat_menu",
            "ratVentureMenus.run_menu",
            "ratVentureMenus.combat_menu",
            "ratVentureMenus.combat_menu"
        ]

        expect_call_withs = [
            [world,player,rat],
            [world,player,rat],
            [world,player,rat],
            [world,player,rat]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                combat_menu(world,player,rat)
                mock.assert_called_once_with(*expect_call_with)



    def test_outdoorMenu(self):
        world = World()
        player = GameEntity(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)

        test_cases = [
            "1",
            "4",
            "f",
            "9"
        ]

        mock_funcs = [
            "ratVentureMenus.outdoor_menu",
            "ratVentureMenus.check_exit",
            "ratVentureMenus.outdoor_menu",
            "ratVentureMenus.outdoor_menu"
        ]

        expect_call_withs = [
            [world,player,rat],
            [world],
            [world,player,rat],
            [world,player,rat]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                outdoor_menu(world,player,rat)
                mock.assert_called_once_with(*expect_call_with)

    
    def test_runMenu(self):
        world = World()
        player = GameEntity(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)

        test_cases = [
            "1",
            "4",
            "h",
            "7"
        ]

        mock_funcs = [
            "ratVentureMenus.combat_menu",
            "ratVentureMenus.check_exit",
            "ratVentureMenus.run_menu",
            "ratVentureMenus.run_menu"
        ]

        expect_call_withs = [
            [world,player,rat],
            [world],
            [world,player,rat],
            [world,player,rat]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                run_menu(world,player,rat)
                mock.assert_called_once_with(*expect_call_with)


    def test_checkSavingBeforeExit(self):
        world = World()

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
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                check_exit(world)
                mock.assert_called_once_with(*expect_call_with)

if __name__ == "__main__":
    unittest.main()
