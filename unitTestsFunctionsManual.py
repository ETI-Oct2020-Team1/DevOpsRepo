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
        self.world = World(8,8)
        self.player = Player(self.world, "The Hero",[2,4],1,20)
        self.rat = GameEntity(self.world,"The Rat",[1,3],1,10)
        self.orb = powerOrb(self.world)
        self.rat_king = RatKing(self.world,"The Rat King",[8,12],5,25)
        self.world.add_entity(self.player)
        self.world.add_entity(self.rat)
        self.world.add_entity(self.orb)
        self.world.add_entity(self.rat_king)
        print("setUp")
        

    def tearDown(self):
        print("\nTear down")
        pass            #Very unlikely I'll need this

    def test_move_date(self):
        TEXT = "Testing date after move"
        txt(TEXT)
        print("Make sure to input a valid move as the date is only added in check_tile()")

        self.player.move()
        #Start at day 1 so after first move it should be day 2.
        self.assertEqual(self.world.day,2)

    def test_cancel_movement(self):
        TEXT = "Make sure to pres 'ESC' Testing location, day and entities after cancelling of movement"
        txt(TEXT)
        org = len(self.world.entities)
        orgPos = self.player.map_location_id
        orgDay = self.world.get_day()
        self.player.move()
        self.assertEqual(len(self.world.entities),org)
        self.assertEqual(self.player.map_location_id,orgPos)
        self.assertEqual(self.world.get_day(),orgDay)

if __name__ == "__main__":
    unittest.main(exit=False)   
#