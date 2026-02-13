## Functions

def reset_game(): #Resets hands and shuffles the deck
    playerHand[:] = []
    dealerHand[:] = []
    deck[:] = list(range(1,52+1))
    random.shuffle(deck)

def read_card_from_index(index): #Reads card and suit value from its index
    # Check that the input is in integer
    if type(index) not in [int]:
        raise TypeError("Input bust be an integer")

    # Initialize variables
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
        raise ValueError("Out of range")
    
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
    # Check that input is a list
    if type(hand) not in [list]:
        raise TypeError("Input must be a list of integers")
    
    # Check that each element is an integer in the range 1-52
    for i in hand:
        if type(i) not in [int]:
            raise TypeError("Hand contains elements that are not integers")
        if i > 52 or i < 1:
            raise ValueError("Card indecies must be between 1 and 52")
        
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

# Create deck and hands and shuffle the deck
playerHand = []
dealerHand = []
deck = []
reset_game()

# Create hands for player and dealer
#dealerHandVisible = [] # This is as relic for the code archaeologists to discover :)

# Various other variables for handling the game
playerTurn = True
dealerTurn = False
gameRunning = True
choice = ""
playerPoints = 0
dealerPoints = 0

## Playing the game
if __name__ == "__main__":
    while(gameRunning):
        # Draw first 2 cards to player and dealer
        playerHand.append(deck.pop())
        playerHand.append(deck.pop())
        dealerHand.append(deck.pop())
        dealerHand.append(deck.pop())

        # Inform player of dealer's shown card
        print("The dealer has a", read_card_from_index(dealerHand[0]), "and 1 card face-down\n")

        # Player's turn
        while playerTurn:
            # Show the player their hand
            print("Cards in your hand:")
            for i in playerHand:
                print(read_card_from_index(i))
            
            # Calculate and show the player their points
            playerPoints = calculate_points(playerHand)
            print("You have", playerPoints, "points")

            # Lose immidietly if the player busts
            if playerPoints > 21:
                time.sleep(1.5) # Letting the player soak for a moment
                print("Bust!")
                time.sleep(2)
                print("You lose")
                time.sleep(2)
                playerTurn = False
                break
            else:
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
        print("The dealer turns their second card face-up, it is a", read_card_from_index(dealerHand[1])) if dealerTurn else None

        # Dealer's turn
        while dealerTurn:
            dealerPoints = calculate_points(dealerHand)
            print("The dealer has", dealerPoints, "points")

            time.sleep(1)

            if dealerPoints < 17:
                dealerHand.append(deck.pop())
                print("The dealer draws a card, it is a", read_card_from_index(dealerHand[-1]))
                #time.sleep(1)
            elif dealerPoints > 21:
                #time.sleep(1)
                print("The dealer has busted!")
                time.sleep(2)
                print("You win!")
                time.sleep(2)
                dealerTurn = False
            else:
                print("The dealer stands")
                time.sleep(1)
                dealerTurn = False
        
        # If neither player nor dealer has busted, compare points and announce the winner
        if playerPoints <= 21 and dealerPoints <= 21:
            print("You have", playerPoints, "points, the dealer has", dealerPoints, "points")
            if playerPoints > dealerPoints:
                print("You win!")
            elif playerPoints == dealerPoints:
                print("Push! It's a draw")
            else:
                print("You lose")

        # Ask to play again
        print("\nPlay again?")
        choice = input()
        if choice == "y":
            reset_game()
            playerTurn = True
        else:
            gameRunning = False