## Functions

def reset_game(): #Resets hands and shuffles the deck
    playerHand[:] = []
    dealerHand[:] = []
    deck[:] = list(range(1,52+1))
    random.shuffle(deck)

def read_card_from_index(index): #Reads card and suit value from its index
    # Init vraiables
    rank = ""
    suit = ""

    # Determinte suit
    if 1 <= index <= 13:
        suit = "Spades"
    elif 13+1 <= index <= 13*2:
        suit = "Hearts"
    elif 13*2+1 <= index <= 13*3:
        suit = "Clubs"
    elif 13*3+1 <= index <= 13*4:
        suit = "Diamonds"
    else:
        #TODO: implement throwing an error
        pass
    
    # Determine rank
    if index%13 == 1:
        rank = "Ace"
    elif index%13 == 11:
        rank = "Jack"
    elif index%13 == 12:
        rank = "Queen"
    elif index%13 == 0:
        rank = "King"
    else:
        rank = str(index%13)
    
    # Return card
    return rank + " of " + suit

def calculate_points(hand): #Calculate how many points in a hand
    # Reduce card indecies to values
    hand = list(map(lambda x: x % 13, hand))
    hand = list(map(lambda x: x + 13 if x == 0 else x, hand)) #Handle kings
    hand = list(map(lambda x: min(10,x), hand))
    #print(hand) #debug

    # Count number of aces in hand
    aceCounter = hand.count(1)
    #print(aceCounter) #debug

    # Tally up points
    points = sum(hand)
    #print(points) #debug

    # Add full points from aces if this does not bring points above 21
    while aceCounter > 0 and points <= 11:
        points += 10
        aceCounter -= 1

    #print(points) #debug
    return points

## Initialize program

# Import libraries
import random
import time

# Create deck hands and shuffle the deck
playerHand = []
dealerHand = []
deck = []
reset_game()

# Create hands for player and dealer
#dealerHandVisible = []

# Various other variables for handling the game
playerTurn = True
dealerTurn = False
gameRunning = True
choice = ""
playerPoints = 0
dealerPoints = 0

## Playing the game
while(gameRunning):
    # Draw first 2 cards to player and dealer
    playerHand.append(deck.pop())
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    dealerHand.append(deck.pop())

    # Inform player of dealer's shown card
    print("The dealer has a", read_card_from_index(dealerHand[0]), "and 1 card face-down\n")

    while playerTurn:
        # Show the player their hand and points
        print("Cards in your hand:")
        for i in playerHand:
            print(read_card_from_index(i))
        print("Points")
        print(calculate_points(playerHand))
        print("")
        
        # Ask player whether to hit or stand
        print("Your options are:")
        print("h - Hit")
        print("s - Stand")
        print("")
        choice = input()

        if choice == "h":
            playerHand.append(deck.pop())
        elif choice == "s":
            playerPoints = calculate_points(playerHand)
            playerTurn = False
            dealerTurn = True
        else:
            print("Sorry, you are not allowed to do that\n")
    
    # Show second dealer card to player
    print("The dealer turns their second card face-up, it is a", read_card_from_index(dealerHand[1]))

    # Dealer's turn
    while dealerTurn:
        dealerPoints = calculate_points(dealerHand)
        print("The dealer has", dealerPoints, "points\n")

        time.sleep(1)

        if dealerPoints < 17:
            dealerHand.append(deck.pop())
            print("The dealer draws a card, it is a", read_card_from_index(dealerHand[-1]))
        else:
            print("The dealer stands")
            dealerTurn = False

    # Ask to play again
    print("Play again?")
    choice = input()
    if choice == "y":
        reset_game()
        playerTurn = True
    else:
        gameRunning = False
'''
#testing stuff (to be deleted later)
print(deck)
print(len(deck))
#print(read_card_from_index(10))
print(playerHand)
print(len(playerHand))
calculate_points(playerHand)
'''