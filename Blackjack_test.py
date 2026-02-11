import unittest
from Blackjack import *

class test_test(unittest.TestCase): #This is just to see if unit testing is actually working
    def test_test(self):
        self.assertEqual(0,0)
        self.assertEqual("one","one")

class reset_game_test(unittest.TestCase):
    def reset_test(self): #Test if the reset happens properly
        reset_game()
        self.assertEqual(playerHand, []) #Player hand should be empty
        self.assertEqual(dealerHand, []) #Dealer hand should be empty
        self.assertEqual(deck.sort, list(range(1,52+1))) #Deck should contain each card exactly once

class read_card_from_index_test(unittest.TestCase):
    def card_test(self): #Test if the function returns the right cards
        self.assertEqual(read_card_from_index(1), "Ace of Spades")
        self.assertEqual(read_card_from_index(13+12), "Queen of Hearts")
        self.assertEqual(read_card_from_index(26+13), "King of Clubs")
        self.assertEqual(read_card_from_index(39+11), "Jack of Clubs")
        self.assertEqual(read_card_from_index(10), "10 of Spades")
        self.assertEqual(read_card_from_index(13+6), "6 of Hearts")

class calculate_points_test(unittest.TestCase):
    def hands_test(self): #Test if various hands returns the expected amount of points
        self.assertEqual(calculate_points([26]), 10) #King of hearts
        self.assertEqual(calculate_points([1]), 11) #One Ace
        self.assertEqual(calculate_points([1, 14]), 12) #Two Aces
        self.assertEqual(calculate_points([1, 14, 27]), 13) #Three Aces
        self.assertEqual(calculate_points([1, 24, 27, 40]), 14) #Four Aces
        self.assertEqual(calculate_points([8, 14]), 19) #8 and one Ace
        self.assertEqual(calculate_points([8, 14, 41]), 21) #Drawing a 2 should take the score to 21
        self.assertEqual(calculate_points([8, 14, 42]), 12) #Drawing a 3 should take the score to 12, since now the Ace counts as 1 point