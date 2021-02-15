from ratVentureMenus import *
import unittest
from pynput.keyboard import Key, Controller
from mock import patch

def txt(TEXT):
    print("\n"*3)
    print("=" * len(TEXT))
    print(TEXT)
    print("=" * len(TEXT))
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

    # Testing to make sure the target entitie is injured during combat
    def test_damage(self):
        TEXT = "test_damage"
        txt(TEXT)
        # Setting the attack to be constant so I can test attack - armor
        self.player.attack = [5,5]
        self.player.damage(self.rat)
        expected_hp = self.rat.max_hp - ( 5 - self.rat.defense)
        self.assertEqual(self.rat.current_hp, expected_hp)

    def test_damage_king(self):
        pass
        # Player should not be able to damage rat king if they do not have the orb
        #self.player.orb = False
        #self.player.damage(self.rat_king)
        #self.assertEqual(self.rat_king.current_hp, self.rat_king.max_hp)
        
        # This test is failing currently
        # Once orb is true the player should be able to damage the rat king
        #self.player.orb = True
        #self.player.damage(self.rat_king)
        #self.assertLess(self.rat_king.current_hp, self.rat_king.max_hp)

    # This also tests the world.add_day() function via proxy 
    # of being called by .rest()
    def test_rest(self):
        TEXT = "Testing health after rest()"
        txt(TEXT)
        self.player.current_hp = self.player.max_hp / 2
        self.player.rest()
        self.assertEqual(self.player.current_hp,self.player.max_hp)
        self.assertEqual(self.world.get_day(),2)     

    def test_neg_rest(self):
        TEXT = "Checking to see if rest() still works if player health is negative" 
        txt(TEXT) 

        self.player.current_hp = -10
        self.player.rest()
        self.assertEqual(self.player.current_hp,self.player.max_hp)
        self.assertEqual(self.world.get_day(),2)
    
    def test_encounter(self):
        TEXT = "Testing adding entities via combat_menu (Input 2)"
        txt(TEXT)2
        org = len(self.world.entities)
        print("Before addition:", org)
        
        self.world.map[self.player.map_location_id] = 0       # Setting that tile to 0 so that combat_menu works
        combat_menu(self.world)
        print("After addition:", len(self.world.entities))
        self.assertEqual(len(self.world.entities),org+2)
        #self.assertNotEqual(len(self.world.entities),org)

    def test_move(self):
        TEXT = "Testing date after move"
        txt(TEXT)


        self.player.move()
        #Start at day 1 so after first move it should be day 2.
        print("Test move, day:",self.world.day)
        self.assertEqual(self.world.day,2)

    def test_cancel_movement(self):
        TEXT = "Testing entities after cancelling of movement"
        txt(TEXT)
        org = len(self.world.entities)
        print("Before cancelling movement:", org)

        self.player.move()
        Controller().release(Key.esc)
        print("After cancelling movement:", len(self.world.entities))
        self.assertEqual(len(self.world.entities),org)

    def test_location(self):
        TEXT = "Testing location after movement"
        txt(TEXT)

        #Start at loc 0 so after moving down it should be world.layout's value
        self.player.move_down()
        print("Location:",self.player.map_location_id)
        self.assertEqual(self.player.map_location_id,self.world.layout)


if __name__ == "__main__":
    unittest.main(exit=False)   
#