import cardFuncs as c
from time import sleep
# Round
cardDeck = []
print("=== Welcome to BlackJack ===\n")
while True:
    c.newCards(cardDeck)
    c.shuffleCards(cardDeck)
    dealerHand = c.dealHand(cardDeck, "dealer")
    print("Dealer's hand:", end=" ")
    c.printHand(dealerHand)
    print(f"Value: {c.getHandValue(dealerHand)}\n")
    hand = c.dealHand(cardDeck, "player")
    print("Your hand:", end = " ")
    c.printHand(hand)
    print(f"Value: {c.getHandValue(hand)}")
    while True:
        if len(hand) < 5:
            usrInput = input("Hit, Stand, or Double [or h/s/d for short]: ").lower()
        else:
            break
        print("")
        if usrInput in ["hit", "h"]:
            print("Player hit:", end = " ")
            drawnCard = c.hit(cardDeck)
            print("".join(str(item) for item in drawnCard))
            hand.append(drawnCard)
            print("Your hand:", end = " ")
            c.printHand(hand)
            print(f"Value: {c.getHandValue(hand)}")
            if c.getHandValue(hand) > 21:
                print("Bust!")
                hand = []
                break
        elif usrInput in ["stand", "s"]:
            print(f"Standing on {c.getHandValue(hand)}")
            break
        elif usrInput in ["double", "d"]:
            print("Player hit:", end=" ")
            drawnCard = c.hit(cardDeck)
            print("".join(str(item) for item in drawnCard))
            hand.append(drawnCard)
            print("Your hand:", end=" ")
            c.printHand(hand)
            print(f"Value: {c.getHandValue(hand)}")
            if c.getHandValue(hand) > 21:
                print("Bust!")
                hand = []
            break
    print("")
    while True:
        sleep(1)
        if c.getHandValue(dealerHand) == 17 and c.hasAce(dealerHand):
            print("Dealer hand:", end=" ")
            c.printHand(dealerHand)
            print("Standing on soft 17")
            break
        elif c.getHandValue(dealerHand) > 21:
            print("Dealer hand:", end=" ")
            c.printHand(dealerHand)
            print("Dealer bust!")
            dealerHand = []
            break
        elif (c.getHandValue(dealerHand) >= c.getHandValue(hand) or len(dealerHand) == 5) and (c.getHandValue(dealerHand) > 16):
            print("Dealer hand:", end = " ")
            c.printHand(dealerHand)
            print("Dealer stands")
            print(f"Value: {c.getHandValue(dealerHand)}\n")
            break
        else:
            print("Dealer hit:", end = " ")
            drawnCard = c.hit(cardDeck)
            print("".join(str(item) for item in drawnCard))
            dealerHand.append(drawnCard)
            print("Dealer hand:", end=" ")
            c.printHand(dealerHand)
            print(f"Value: {c.getHandValue(dealerHand)}\n")
    if c.getHandValue(hand) > c.getHandValue(dealerHand):
        print("Player wins!")
    elif c.getHandValue(hand) < c.getHandValue(dealerHand):
        print("Dealer wins!")
    elif c.getHandValue(hand) == c.getHandValue(dealerHand):
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
        print("Thank you for playing")
        break
