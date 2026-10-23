from random import randint
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

