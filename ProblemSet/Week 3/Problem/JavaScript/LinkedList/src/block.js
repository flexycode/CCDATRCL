// block.js
const { SHA256 } = require('crypto-js');

class Block {
    constructor(timestamp, data, previousHash) {
        this.timestamp = timestamp;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    calculateHash() {
        const blockString = `${this.timestamp}${JSON.stringify(this.data)}${this.previousHash}`;
        return SHA256(blockString).toString();
    }
}

module.exports = Block;
