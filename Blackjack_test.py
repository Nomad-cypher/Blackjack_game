import unittest
from Blackjack import *

class test_test(unittest.TestCase): #This is just to see if unit testing is actually working
    def test_test(self):
        self.assertEqual(0,0)
        self.assertEqual("one","one")

class reset_game_test(unittest.TestCase):
    def test_reset(self): #Test if the reset happens properly
        reset_game()
        self.assertEqual(playerHand, []) #Player hand should be empty
        self.assertEqual(dealerHand, []) #Dealer hand should be empty
        deck.sort()
        self.assertEqual(deck, list(range(1,52+1))) #Deck should contain each card exactly once

class read_card_from_index_test(unittest.TestCase):
    def test_cards(self): #Test if the function returns the right cards
        self.assertEqual(read_card_from_index(1), "Ace of Spades")
        self.assertEqual(read_card_from_index(13+12), "Queen of Hearts")
        self.assertEqual(read_card_from_index(26+13), "King of Clubs")
        self.assertEqual(read_card_from_index(39+11), "Jack of Diamonds")
        self.assertEqual(read_card_from_index(10), "10 of Spades")
        self.assertEqual(read_card_from_index(13+6), "6 of Hearts")

    def test_oufofbounds(self): #Test if the function throws an error if the input is out of bounds
        self.assertRaises(ValueError, read_card_from_index, 0) #Zero
        self.assertRaises(ValueError, read_card_from_index, -25) #Negative
        self.assertRaises(ValueError, read_card_from_index, 53) #Too large

    def test_value_errors(self): #Test if the function throws an error if a wrong value type is entered
        self.assertRaises(TypeError, read_card_from_index, 3.14) #Non-integer
        self.assertRaises(TypeError, read_card_from_index, True) #Boolean
        self.assertRaises(TypeError, read_card_from_index, 6+9j) #Complex number
        self.assertRaises(TypeError, read_card_from_index, "Ace of Spades") #String


class calculate_points_test(unittest.TestCase):
    def test_hands(self): #Test if various hands returns the expected amount of points
        self.assertEqual(calculate_points([26]), 10) #King
        self.assertEqual(calculate_points([1]), 11) #One Ace
        self.assertEqual(calculate_points([1, 14]), 12) #Two Aces
        self.assertEqual(calculate_points([1, 14, 27]), 13) #Three Aces
        self.assertEqual(calculate_points([1, 14, 27, 40]), 14) #Four Aces
        self.assertEqual(calculate_points([8, 14]), 19) #An 8 and one Ace
        self.assertEqual(calculate_points([8, 14, 41]), 21) #Drawing a 2 should take the score to 21
        self.assertEqual(calculate_points([8, 14, 42]), 12) #Drawing a 3 should take the score to 12, since now the Ace counts as 1 point
        self.assertEqual(calculate_points([12, 12]), 20) #Multiple copies of the same card is fine
        self.assertEqual(calculate_points([]), 0) #An empty hand is worth zero points

    def test_oufofbounds(self): #Test hands card card indicies that are out of bounds
        self.assertRaises(ValueError, calculate_points, [0]) #Zero
        self.assertRaises(ValueError, calculate_points, [-25]) #Negative
        self.assertRaises(ValueError, calculate_points, [53]) #Too large
        self.assertRaises(ValueError, calculate_points, [0, 0, 0]) #Multiple zeroes
        self.assertRaises(ValueError, calculate_points, [1, 26, 53, 52]) #Mixed with good indecies

    def test_value_errors(self): #Test if the function throws an error if a wrong value type is entered
        self.assertRaises(TypeError, read_card_from_index, "Blackjack") #Not a list
        self.assertRaises(TypeError, read_card_from_index, [[2],[5,[1, 7]]]) #List of lists
        self.assertRaises(TypeError, read_card_from_index, [3.14]) #List contains float
        self.assertRaises(TypeError, read_card_from_index, [True]) #List contains boolean
        self.assertRaises(TypeError, read_card_from_index, [6+9j]) #List contains complex number
        self.assertRaises(TypeError, read_card_from_index, ["Blackjack"]) #List contains string
        self.assertRaises(TypeError, read_card_from_index, [25, "Ace of Spades", 13, 52]) #List contains mix