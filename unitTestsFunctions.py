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
        print("Tear down")
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

    def test_orb_boost(self):
        TEXT = "Checking player stats after being boosted by the orb of power"
        txt(TEXT)

        orig_Atk = self.player.attack 
        orig_Def = self.player.defense
        print("Original stats:\nAttack: {0}\nDefence: {1}".format(orig_Atk,orig_Def))

        self.orb.power(self.player)
        print("\nBoosted stats:\nAttack: {0}\nDefence: {1}".format(self.player.attack,self.player.defense))
        self.assertEqual(self.player.attack,[x + 5 for x in orig_Atk])
        self.assertEqual(self.player.defense,(orig_Def + 5))

    def test_damage_king_orb_f(self):
        TEXT = "Attacking the rat king WITHOUT the orb"
        txt(TEXT)
        # Player should not be able to damage rat king if they do not have the orb
        self.player.orb = False
        self.player.attack = [50,50]
        self.player.damage(self.rat_king)
        self.assertEqual(self.rat_king.current_hp, self.rat_king.max_hp)
        
    def test_damge_king_orb_true(self):
        TEXT = "Attacking the rat king WITH the orb"
        txt(TEXT)
        # Once orb is true the player should be able to damage the rat king
        self.player.attack = [50,50]
        self.player.orb = True
        self.player.damage(self.rat_king)
        self.assertLess(self.rat_king.current_hp, self.rat_king.max_hp)
        
    def test_player_death(self):
        self.rat.attack = [50,50]
        self.assertTrue(self.rat.damage(self.player))

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
        txt(TEXT)
        org = len(self.world.entities)
        print("Before addition:", org)

        self.world.encounter()
        self.assertEqual(len(self.world.entities),org+1)

    def test_move_date(self):
        TEXT = "Testing date after move"
        txt(TEXT)


        self.player.move()
        #Start at day 1 so after first move it should be day 2.
        self.assertEqual(self.world.day,2)

    def test_cancel_movement(self):
        TEXT = "Testing entities after cancelling of movement"
        txt(TEXT)
        org = len(self.world.entities)
        self.player.move()
        self.assertEqual(len(self.world.entities),org)

    def test_player_location(self):
        TEXT = "Testing location after movement"
        txt(TEXT)

        #Start at loc 0 so after moving down it should be world.layout's value
        self.player.move_down()
        print("Location:",self.player.map_location_id)
        self.assertEqual(self.player.map_location_id,self.world.layout)

    def test_win_game(self):
        self.rat_king.current_hp = 0
        self.assertTrue(self.world.gameWin())

if __name__ == "__main__":
    unittest.main(exit=False)   
#