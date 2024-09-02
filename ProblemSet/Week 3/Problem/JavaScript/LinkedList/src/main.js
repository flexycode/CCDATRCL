const readline = require('readline');
const fs = require('fs');
const AuctionSystem = require('./auctionSystem');
const Auction = require('./auction');

const auctionSystem = new AuctionSystem();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const DATA_FILE = 'auction_data.json';

function saveData() {
    const data = JSON.stringify(auctionSystem.getAuctions());
    fs.writeFileSync(DATA_FILE, data);
    console.log('Data saved successfully!');
}

function loadData() {
    if (fs.existsSync(DATA_FILE)) {
        const data = fs.readFileSync(DATA_FILE, 'utf8');
        const auctions = JSON.parse(data);
        auctionSystem.setAuctions(auctions);
        console.log('Data loaded successfully!');
    } else {
        console.log('No data found. Starting with an empty auction system.');
    }
}

function displayMenu() {
    console.log('=== Auction System Menu ===');
    console.log('1. Create Auction');
    console.log('2. Place Bid');
    console.log('3. End Auction');
    console.log('4. List My Bids');
    console.log('5. List Auctions');
    console.log('6. Search Auctions');
    console.log('7. Delete Auction');
    console.log('8. Save Data');
    console.log('9. Exit');
}

function createAuction() {
    rl.question('Enter the item name: ', (item) => {
        rl.question('Enter the start price: ', (startPrice) => {
            rl.question('Enter the auction duration (in minutes): ', (duration) => {
                rl.question('Enter the description of the item: ', (description) => {
                    const auction = new Auction(item, parseInt(startPrice), parseInt(duration), description);
                    auctionSystem.createAuction(auction);
                    console.log('Auction created successfully!');
                    displayMenu();
                    processInput();
                });
            });
        });
    });
}

function placeBid() {
    rl.question('Enter the item name: ', (item) => {
        rl.question('Enter your name: ', (bidder) => {
            rl.question('Enter your bid amount: ', (amount) => {
                const success = auctionSystem.placeBid(item, bidder, parseInt(amount));
                if (success) {
                    console.log('Bid placed successfully!');
                } else {
                    console.log('Failed to place the bid. Please check the item or bid amount.');
                }
                displayMenu();
                processInput();
            });
        });
    });
}

function endAuction() {
    rl.question('Enter the item name: ', (item) => {
        const winner = auctionSystem.endAuction(item);
        if (winner) {
            console.log(`Auction ended. Winner: ${winner.bidder}`);
        } else {
            console.log('Failed to end the auction. Please check the item or auction status.');
        }
        displayMenu();
        processInput();
    });
}

function listBids() {
    const bids = auctionSystem.listBids();
    if (bids.length > 0) {
        console.log('=== My Bids ===');
        bids.forEach((bid) => {
            console.log(`Item: ${bid.item}, Bidder: ${bid.bidder}, Amount: ${bid.amount}`);
        });
    } else {
        console.log('You have not placed any bids yet.');
    }
    displayMenu();
    processInput();
}

function listAuctions() {
    const auctions = auctionSystem.listAuctions();
    if (auctions.length > 0) {
        console.log('=== Auctions ===');
        auctions.forEach((auction) => {
            console.log(`Item: ${auction.item}, Start Price: ${auction.startPrice}, Description: ${auction.description}`);
        });
    } else {
        console.log('No auctions found.');
    }
    displayMenu();
    processInput();
}

function searchAuctions() {
    rl.question('Enter a keyword to search for auctions: ', (keyword) => {
        const matchingAuctions = auctionSystem.searchAuctions(keyword);
        if (matchingAuctions.length > 0) {
            console.log('=== Matching Auctions ===');
            matchingAuctions.forEach((auction) => {
                console.log(`Item: ${auction.item}, Start Price: ${auction.startPrice}, Description: ${auction.description}`);
            });
        } else {
            console.log('No matching auctions found.');
        }
        displayMenu();
        processInput();
    });
}

function deleteAuction() {
    rl.question('Enter the item name of the auction to delete: ', (item) => {
        const success = auctionSystem.deleteAuction(item);
        if (success) {
            console.log(`Auction "${item}" deleted successfully.`);
        } else {
            console.log(`Failed to delete auction "${item}". Auction not found.`);
        }
        displayMenu();
        processInput();
    });
}

function processInput() {
    rl.question('Enter your choice: ', (choice) => {
        switch (choice) {
            case '1':
                createAuction();
                break;
            case '2':
                placeBid();
                break;
            case '3':
                endAuction();
                break;
            case '4':
                listBids();
                break;
            case '5':
                listAuctions();
                break;
            case '6':
                searchAuctions();
                break;
            case '7':
                deleteAuction();
                break;
            case '8':
                saveData();
                break;
            case '9':
                rl.close();
                break;
            default:
                console.log('Invalid choice. Please try again.');
                displayMenu();
                processInput();
                break;
        }
    });
}

loadData();
displayMenu();
processInput();
