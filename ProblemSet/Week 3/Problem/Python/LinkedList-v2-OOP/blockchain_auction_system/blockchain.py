from datetime import datetime

from block import Block
from doubly_linked_list import DoublyLinkedList


def create_genesis_block():
    """
    Create the genesis block (first block in the chain).
    """
    return Block(datetime.now(), "Genesis Block", "0")


class Blockchain:
    """
    Represents the blockchain.
    """
    def __init__(self):
        self.chain = DoublyLinkedList()
        self.genesis_block = create_genesis_block()
        self.chain.insert_at_end(self.genesis_block)

    def add_block(self, data: object) :
        """
        Add a new block to the blockchain.
        """
        previous_block = self.chain.tail.data
        new_block = Block(datetime.now(), data, previous_block.hash)
        self.chain.insert_at_end(new_block)

    def is_chain_valid(self):
        """
        Check if the blockchain is valid.
        """
        current = self.chain.head
        while current:
            if current.data.hash != current.data.calculate_hash():
                return False
            if current.next and current.data.hash != current.next.data.previous_hash:
                return False
            current = current.next
        return True

    def __str__(self):
        """
        Return a string representation of the blockchain.
        """
        blocks = []
        current = self.chain.head
        while current:
            blocks.append(str(current.data))
            current = current.next
        return '\n'.join(blocks)