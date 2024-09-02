class Auction {
    constructor(item, startPrice, duration, description) {
        this.item = item;
        this.startPrice = startPrice;
        this.duration = duration * 60000; // Convert minutes to milliseconds
        this.description = description;
        this.bids = [];
        this.startTime = Date.now();
    }

    placeBid(bidder, amount) {
        if (amount > this.getCurrentPrice() && this.isActive()) {
            this.bids.push({ bidder, amount });
            return true;
        }
        return false;
    }

    isActive() {
        const elapsedTime = Date.now() - this.startTime;
        return elapsedTime < this.duration;
    }

    getCurrentPrice() {
        return this.bids.length > 0 ? this.bids[this.bids.length - 1].amount : this.startPrice;
    }

    getDescription() {
        return this.description;
    }

    getWinner() {
        if (this.bids.length > 0) {
            return this.bids.reduce((highestBid, currentBid) => {
                return currentBid.amount > highestBid.amount ? currentBid : highestBid;
            });
        }
        return null;
    }
}

module.exports = Auction;
