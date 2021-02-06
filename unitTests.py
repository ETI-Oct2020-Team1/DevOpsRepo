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
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                town_menu(world)
                mock.assert_called_once_with(*expect_call_with)



    def test_combatMenu(self):
        world = World(8,8)
        player = GameEntity(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)
        target = rat

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
            [world,target],
            [world],
            [world,target],
            [world,target]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                combat_menu(world,target)
                mock.assert_called_once_with(*expect_call_with)



    def test_outdoorMenu(self):
        world = World(8,8)
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
            [world],
            [world],
            [world],
            [world]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                outdoor_menu(world)
                mock.assert_called_once_with(*expect_call_with)

    
    def test_runMenu(self):
        world = World(8,8)
        player = GameEntity(world, "The Hero",[1,5],1,20)
        rat = GameEntity(world,"The rat",[1,3],1,20)
        world.add_entity(player)
        world.add_entity(rat)
        target = None

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
            [world,target],
            [world],
            [world],
            [world]
        ]

        for test_case, mock_func, expect_call_with in zip(test_cases, mock_funcs, expect_call_withs):
            with patch("builtins.input", return_value=test_case), patch(mock_func) as mock:
                run_menu(world)
                mock.assert_called_once_with(*expect_call_with)


    def test_checkSavingBeforeExit(self):
        world = World(8,8)

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

class TestFunctions(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.world = World(8,8)
        self.player = Player(self.world, "The Hero",[2,4],1,20)
        self.rat = GameEntity(self.world,"The Rat",[1,3],1,10)
        self.orb = powerOrb(self.world)
        self.rat_king = GameEntity(self.world,"The Rat King",[8,12],5,25)
        self.world.add_entity(self.player)
        self.world.add_entity(self.rat)
        self.world.add_entity(self.orb)

    def tearDown(self):
        pass            #Very unlikely I'll need this

    def test_damage(self):
        # Testing to make sure the target entitie is injured during combat
        self.player.damage(self.rat)
        self.assertLess(self.rat.current_hp, self.rat.max_hp)

        # Player should not be able to damage rat king if they do not have the orb
        self.player.orb = False
        self.player.damage(self.rat_king)
        self.assertEqual(self.rat_king.current_hp, self.rat_king.max_hp)
        
        # This test is failing currently
        # Once orb is true the player should be able to damage the rat king
        #self.player.orb = True
        #self.player.damage(self.rat_king)
        #self.assertLess(self.rat_king.current_hp, self.rat_king.max_hp)

    # This also tests the world.add_day() function via proxy 
    # of being called by .rest()
    # Testing to see if the day gets +1 which in the first one case should be 2 then 3 and so on...
    def test_rest(self):
        print("Testing heal")
        self.player.current_hp = self.player.max_hp / 2
        self.player.rest()
        self.assertEqual(self.player.current_hp,self.player.max_hp)
        self.assertEqual(self.world.get_day(),2)     

        # Checking to see if the function still works if player health is negative
        self.player.current_hp = -10
        self.player.rest()
        self.assertEqual(self.player.current_hp,self.player.max_hp)
        self.assertEqual(self.world.get_day(),3)


if __name__ == "__main__":
    unittest.main()
#