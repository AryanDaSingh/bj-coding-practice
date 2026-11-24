export default class Cards {
    #deck = [];
    #playerHand = [];
    #dealerHand = [];

    newRound() {
        this.#newDeck();
        this.#shuffleDeck();
        this.#clearHands();
    }

    #clearHands() {
        this.#playerHand = [];
        this.#dealerHand = [];
    }

    #newDeck() {
        const ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"];
        const suits = ["S", "H", "C", "D"];

        ranks.forEach(rank => {
            suits.forEach(suit => {
                this.#deck.push([rank, suit]);
            })
        })
    }

    #shuffleDeck() {
        for (let i = this.#deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.#deck[i], this.#deck[j]] = [this.#deck[j], this.#deck[i]];
        }
    }

    dealHands() {
        this.drawCard(this.#playerHand);
        this.drawCard(this.#playerHand);
        this.drawCard(this.#dealerHand);
    }

    resetHands() {
        this.#playerHand = [];
        this.#dealerHand = [];
    }

    drawCard(hand) {
        const randIndex = Math.floor(Math.random() * this.#deck.length);
        hand.push(this.#deck.splice(randIndex, 1)[0]);
    }

    handSize(hand) {
        return hand.length;
    }

    handValue(hand) {
        let hasAce = false;
        let value = 0;
        for (let i = 0; i < hand.length; i++) {
            if (["J", "Q", "K"].includes(hand[i][0])) {
                value += 10
            } else if (hand[i][0] === "A") {
                hasAce = true;
            } else {
                value += hand[i][0]
            }
        }
        if (hasAce) {
            if (value > 10) {
                value += 1;
            } else {
                value += 11;
            }
        }
        return value;
    }

    get playerHand() {
        return this.#playerHand;
    }

    get dealerHand() {
        return this.#dealerHand;
    }

    get deck() {
        return this.#deck;
    }
}