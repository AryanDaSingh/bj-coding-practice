import Cards from './Cards.js';

const root = document.getElementById("root");
const game = new Cards();

const title = document.createElement("h1");
title.classList.add('title');
title.innerText = ("Welcome to blackjack brother");
root.append(title);

const display = document.createElement("div");
display.classList.add("display");

function resetDisplayedHands() {
    game.resetHands();
    playerCards.innerText = "";
    playerCards.innerText = "";
}

function displayHand(hand, type) {
    let handDisplay = "";
    for (let i = 0; i < hand.length; i++) {
        handDisplay += `${hand[i][0]}${hand[i][1]} `;
    }
    if (type === "player") {
        playerCards.innerText = handDisplay;
    } else {
        dealerCards.innerText = handDisplay;
    }
}

// Init
game.newRound();
const player = document.createElement("div");
const playerCards = document.createElement("span");
const dealer = document.createElement("div");
const dealerCards = document.createElement("span");
player.innerText = "Your hand: ";
dealer.innerText = "Dealer's hand: ";
resetDisplayedHands();

// Setup hands
game.dealHands();
displayHand(game.playerHand, "player");
displayHand(game.dealerHand, "dealer");

// Message box
const message = document.createElement("div");
message.innerText = "Click a button below to perform an action";
function flashMessage(msg) {
    const prev = message.innerText;
    setTimeout(() => {
        message.innerText = prev;
    }, 1000)
    message.innerText = msg;
}

// Buttons
const btnContainer = document.createElement("div");
btnContainer.classList.add("btn-container");

// Hit button
const btnHit = document.createElement("button");
btnHit.innerText = "Hit";
btnHit.classList.add("hit");

function checkForHit(hand) {
    let playerHandSize = game.handSize(hand);
    let handValue = game.handValue(hand);
    if (playerHandSize > 5 || handValue >= 21) {
        return false;
    } else {
        return true;
    }
}

btnHit.addEventListener("click", (e) => {
    let canHit = checkForHit(game.playerHand);
    if (canHit) {
        game.drawCard(game.playerHand);
        displayHand(game.playerHand, "player");
    }
    canHit = checkForHit(game.playerHand);
    if (!canHit) {
        e.target.disabled = true;
    }
});

// Stand button
const btnStand = document.createElement("button");
btnStand.innerText = "Stand";
btnStand.classList.add("stand");

// Rendering
player.append(playerCards);
dealer.append(dealerCards);
btnContainer.append(btnHit);
btnContainer.append(btnStand);
display.append(player);
display.append(dealer);
display.append(message);
display.append(btnContainer);
root.append(display);