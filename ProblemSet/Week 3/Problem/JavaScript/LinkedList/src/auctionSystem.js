require('./blockchain');
const Auction = require('./auction');

class AuctionSystem {
    constructor() {
        this.auctions = [];
    }

    createAuction(item, startPrice, duration, description) {
        const auction = new Auction(item, startPrice, duration, description);
        this.auctions.push(auction);
    }

    placeBid(item, bidder, amount) {
        const auction = this.auctions.find((auction) => auction.item === item);
        if (auction && auction.isActive()) {
            auction.placeBid(bidder, amount);
            return true;
        }
        return false;
    }

    endAuction(item) {
        const auction = this.auctions.find((auction) => auction.item === item);
        if (auction && auction.isActive()) {
            const winner = auction.getWinner();
            if (winner) {
                const index = this.auctions.indexOf(auction);
                this.auctions.splice(index, 1); // Remove the auction from the list
                return winner;
            }
        }
        return null;
    }

    listBids() {
        const bids = [];
        this.auctions.forEach((auction) => {
            auction.bids.forEach((bid) => {
                bids.push({
                    item: auction.item,
                    bidder: bid.bidder,
                    amount: bid.amount,
                });
            });
        });
        return bids;
    }

    listAuctions() {
        return this.auctions.map((auction) => auction.item);
    }

    searchAuctions(keyword) {
        keyword.toLowerCase();
        return this.auctions.filter((auction) => {
            const lowerCaseItem = auction.item.toLowerCase();
            return lowerCaseItem.includes(lowerCaseItem);
        });
    }

    deleteAuction(item) {
        const index = this.auctions.findIndex((auction) => auction.item === item);
        if (index !== -1) {
            this.auctions.splice(index, 1);
            return true;
        }
        return false;
    }

    getAuctions() {
        return this.auctions;
    }

    setAuctions(auctions) {
        this.auctions = auctions;
    }
}

module.exports = AuctionSystem;
