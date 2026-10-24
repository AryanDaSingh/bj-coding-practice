from random import randint
from time import sleep
cardDeck = []

def newCards():
    global cardDeck
    cardNum = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    cardSuit = ["♠", "♥", "♣", "♦"]
    for num in range(len(cardNum)):
        for suit in range(len(cardSuit)):
            arr = [cardNum[num], cardSuit[suit]]
            cardDeck.append(arr)

def shuffleCards():
    global cardDeck
    for i in range(len(cardDeck) - 1, 0, -1):
        j = randint(0, i)
        cardDeck[i], cardDeck[j] = cardDeck[j], cardDeck[i]

def dealHand(type):
    global cardDeck
    arr = []
    n = 0
    if type == "player":
        n = 2
    elif type == "dealer":
        n = 1
    for i in range(n):
        j = randint(0, len(cardDeck) - 1)
        card = cardDeck[j]
        cardDeck.pop(j)
        arr.append(card)
    return arr

def getHandValue(hand):
    value = 0
    for i in range(len(hand)):
        if hand[i][0] in ["J", "Q", "K"]:
            value += 10
        elif hand[i][0] != "A":
            value += hand[i][0]
        else:
            if value + 11 > 21:
                value += 1
            else:
                value += 11
    return value

def printHand(hand):
    for i in range(len(hand)):
        print("".join(str(item) for item in hand[i]), end="; ")
    print("")

def hit():
    global cardDeck
    j = randint(0, len(cardDeck) - 1)
    card = cardDeck[j]
    cardDeck.pop(j)
    return card

def hasAce(hand):
    for i in range(len(hand)):
        if "A" in hand[i]:
            return True

# Round
print("=== Welcome to BlackJack ===\n")
while True:
    newCards()
    shuffleCards()
    dealerHand = dealHand("dealer")
    print("Dealer's hand:", end=" ")
    printHand(dealerHand)
    print(f"Value: {getHandValue(dealerHand)}\n")
    hand = dealHand("player")
    print("Your hand:", end = " ")
    printHand(hand)
    print(f"Value: {getHandValue(hand)}")
    while True:
        if len(hand) < 5:
            usrInput = input("Hit, Stand, or Double [or h/s/d for short]: ").lower()
        else:
            break
        print("")
        if usrInput in ["hit", "h"]:
            print("Player hit:", end = " ")
            drawnCard = hit()
            print("".join(str(item) for item in drawnCard))
            hand.append(drawnCard)
            print("Your hand:", end = " ")
            printHand(hand)
            print(f"Value: {getHandValue(hand)}")
            if getHandValue(hand) > 21:
                print("Bust!")
                hand = []
                break
        elif usrInput in ["stand", "s"]:
            print(f"Standing on {getHandValue(hand)}")
            break
        elif usrInput in ["double", "d"]:
            print("Player hit:", end=" ")
            drawnCard = hit()
            print("".join(str(item) for item in drawnCard))
            hand.append(drawnCard)
            print("Your hand:", end=" ")
            printHand(hand)
            print(f"Value: {getHandValue(hand)}")
            if getHandValue(hand) > 21:
                print("Bust!")
                hand = []
            break
    print("")
    while True:
        sleep(1)
        if getHandValue(dealerHand) == 17 and hasAce(dealerHand):
            print("Dealer hand:", end=" ")
            printHand(dealerHand)
            print("Standing on soft 17")
            break
        elif getHandValue(dealerHand) > 21:
            print("Dealer hand:", end=" ")
            printHand(dealerHand)
            print("Dealer bust!")
            dealerHand = []
            break
        elif (getHandValue(dealerHand) >= getHandValue(hand) or len(dealerHand) == 5) and (getHandValue(dealerHand) > 16):
            print("Dealer hand:", end = " ")
            printHand(dealerHand)
            print("Dealer stands")
            print(f"Value: {getHandValue(dealerHand)}\n")
            break
        else:
            print("Dealer hit:", end = " ")
            drawnCard = hit()
            print("".join(str(item) for item in drawnCard))
            dealerHand.append(drawnCard)
            print("Dealer hand:", end=" ")
            printHand(dealerHand)
            print(f"Value: {getHandValue(dealerHand)}\n")
    if getHandValue(hand) > getHandValue(dealerHand):
        print("Player wins!")
    elif getHandValue(hand) < getHandValue(dealerHand):
        print("Dealer wins!")
    elif getHandValue(hand) == getHandValue(dealerHand):
        print("Draw!") # Return bets
    playAgain = False
    while True:
        usrInput = input("Play again [y/n]: ")
        if usrInput == "y":
            playAgain = True
            break
        elif usrInput == "n":
            playAgain = False
            break
        else:
            print("\nInvalid input\n")
    if not playAgain:
        break
    else:
        print("Thank you for playing")
