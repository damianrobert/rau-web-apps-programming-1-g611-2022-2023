function draw(imagePath) {
    
    function drawImage() {
        ctx.drawImage(img, 100, 100);
    }
    
    const canvas = document.getElementById("viewport");
    const ctx = canvas.getContext("2d");

    const img = new Image();
    img.src = imagePath;
    img.onload = drawImage;
}


class Card {
    name;
    suit;
    value;
    image;

    constructor(image) {
        this.image = image;
        this.getValueFromImageName();
    }

    getValueFromImageName() {
        const imageName = this.image.split(".")[0];
        const imageNameComponents = imageName.split("_");
        this.name = imageNameComponents[2];
        this.suit = imageNameComponents[1];
        this.value = this.convertStringValueToInt(imageNameComponents[2]);
    }

    convertStringValueToInt(stringValue) {
        let value;
        switch (stringValue) {
            case "02": {
                value = 2;
                break;
            }
            case "03": {
                value = 3;
                break;
            }
            case "04": {
                value = 4;
                break;
            }
            case "05": {
                value = 5;
                break;
            }
            case "06": {
                value = 6;
                break;
            }
            case "07": {
                value = 7;
                break;
            }
            case "08": {
                value = 8;
                break;
            }
            case "09": {
                value = 9;
                break;
            }
            case "10": {
                value = 10;
                break;
            }
            case "J": {
                value = 10;
                break;
            }
            case "Q": {
                value = 10;
                break;
            }
            case "K": {
                value = 10;
                break;
            }
            case "A": {
                value = 11;
                break;
            }
        }
        return value;
    }

    changeValue() {
        if (this.value === 11) {
            this.value = 1;
        }
    }

}

class Deck {
    CARDS_PER_DECK = 52;
    SUIT = ["clubs", "diamonds", "hearts", "spades"];
    SYMBOLS = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "J", "Q", "K", "A"];
    cards;
    nDecks;
    nCards;
    constructor(nDecks) {
        this.cards = [];
        this.nDecks = nDecks;
        this.getDecks(nDecks);
        this.nCards = nDecks * this.CARDS_PER_DECK;
        this.reinitDeck = this.nCards / 2;
    }

    getDecks(nDecks) {
        for (let i = 0; i < nDecks; i++) {
            for (const suit of this.SUIT) {
                for (const symbol of this.SYMBOLS) {
                    const cardImagePath = this.generateImagePath(suit, symbol);
                    const card = new Card(cardImagePath);
                    this.cards.push(card);
                }
            }
        }
    }

    generateImagePath(suit, symbol) {
        const path = `D:\\LUCHICI\\Web Apps Programming 1\\Source\\rau-web-apps-programming-1-g611-2022-2023\\htdocs\\assets\\game\\PNG\\Cards (large)\\card_${suit}_${symbol}.png`;
        return path;
    }

    removeCard() {
        if (this.nCards < this.reinitDeck) {
            this.cards = [];
            this.getDecks(this.nDecks);
            this.nCards = this.nDecks * this.CARDS_PER_DECK;
        }
        const cardIndex = Math.floor(Math.random() * (this.nCards + 1));
        const card = this.cards[cardIndex];
        this.cards.splice(cardIndex, 1);
        this.nCards = this.nCards - 1;
        return card;
    }
}



const deck = new Deck(1);
console.log(deck);

const card = deck.removeCard();

draw(card.image);