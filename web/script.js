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
    handDisplay += `(${game.handValue(hand)})`
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
let playerComplete = false;

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
    let handSize = game.handSize(hand);
    let handValue = game.handValue(hand);
    if ((handSize >= 2 && handSize > 5) || handValue >= 21) {
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
        dealerPlay();
    }
});

// Stand button
const btnStand = document.createElement("button");
btnStand.innerText = "Stand";
btnStand.classList.add("stand");

btnStand.addEventListener("click", (e) => {
    dealerPlay();
})

// Dealer logic
function dealerPlay() {
    btnHit.disabled = true;
    btnStand.disabled = true;
    let dealerComplete = false;
    while (!dealerComplete) {
        if (checkForHit(game.dealerHand)) {
            // Dealer CAN hit
            if (game.handValue(game.dealerHand) < game.handValue(game.playerHand)) {
                // Dealer SHOULD hit
                game.drawCard(game.dealerHand);
                displayHand(game.dealerHand, "dealer");
            } else {
                // Dealer SHOULD stand
                dealerComplete = true;
            }
        } else {
            // Dealer MUST stand
            dealerComplete = true;
        }
    }
    console.log(checkWin());
}

// Check for win
function checkWin() {
    let playerHandValue = game.handValue(game.playerHand);
    let playerHandSize = game.handSize(game.playerHand);
    let dealerHandValue = game.handValue(game.dealerHand);
    let dealerHandSize = game.handSize(game.dealerHand);
    // Busts
    if (playerHandSize > 21) return "Dealer wins!";
    if (dealerHandSize > 21) return "Player wins!";
    // Values
    if (playerHandValue > dealerHandValue) return "Player wins!";
    if (playerHandValue < dealerHandValue) return "Dealer wins!";
    // Tiebreaker
    return playerHandSize > dealerHandSize ? "Player wins!" : "Dealer wins!";
}

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