// blockchain.js

const Block = require('./block');

class Blockchain {
    constructor() {
        this.chain = [];
        this.createGenesisBlock();
    }

    createGenesisBlock() {
        // Create the genesis block (the first block) of the blockchain
        const genesisBlock = new Block(Date.now(), 'Genesis Block', '0');
        this.chain.push(genesisBlock);
    }
}

module.exports = Blockchain;
