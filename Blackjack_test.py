import unittest
from Blackjack import *

class reset_game_test(unittest.TestCase):
    def reset_test(self): #Test if the reset happens properly
        reset_game()
        self.assertEqual(playerHand, []) #Player hand should be empty
        self.assertEqual(dealerHand, []) #Dealer hand should be empty
        self.assertEqual(deck.sort, list(range(1,52+1))) #Deck should contain each card exactly once