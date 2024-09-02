import hashlib
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the doubly linked list
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, key):
        # Delete a node with the given key from the doubly linked list
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def search(self, key):
        # Search for a node with the given key in the doubly linked list
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def traverse(self):
        # Traverse and print the elements of the doubly linked list
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class DoubleEndedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_front(self, data):
        # Insert a new node at the front of the double-ended linked list
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the double-ended linked list
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        # Delete a node with the given key from the double-ended linked list
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        current = self.head
        while current.next:
            if current.next.data == key:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

    def search(self, key):
        # Search for a node with the given key in the double-ended linked list
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def traverse(self):
        # Traverse and print the elements of the double-ended linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # Insert a new node at the end of the circular linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        # Delete a node with the given key from the circular linked list
        if not self.head:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
        if current.data == key:
            prev.next = self.head

    def search(self, key):
        # Search for a node with the given key in the circular linked list
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data.item == key: # Compare the item names instead of the entire node
                return current.data
            current = current.next
            if current == self.head:
                break
        return None

    def traverse(self):
        # Traverse and print the elements of the circular linked list
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (back to head)")


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the hash of the block using the timestamp, data, and previous hash
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = DoublyLinkedList()
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the genesis block (the first block) of the blockchain
        genesis_block = Block(time.time(), "Genesis Block", "0")
        self.chain.insert_at_beginning(genesis_block)

    def add_block(self, data):
        # Add a new block to the blockchain with the given data
        previous_block = self.chain.tail.data
        new_block = Block(time.time(), data, previous_block.hash)
        self.chain.insert_at_beginning(new_block)

    def is_chain_valid(self):
        # Check if the blockchain is valid by verifying the hashes and previous hashes of each block
        current = self.chain.head
        while current.next:
            if current.data.hash != current.data.calculate_hash():
                return False
            if current.data.previous_hash != current.next.data.hash:
                return False
            current = current.next
        return True


class Auction:
    def __init__(self, item, start_price, end_time):
        self.item = item
        self.start_price = start_price
        self.current_price = start_price
        self.end_time = end_time
        self.bids = DoubleEndedLinkedList()

    def place_bid(self, bidder, amount):
        # Place a bid on the auction with the given bidder and amount
        if amount > self.current_price and time.time() < self.end_time:
            self.current_price = amount
            self.bids.insert_at_end((bidder, amount))
            return True
        return False


class AuctionSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.auctions = CircularLinkedList()

    def create_auction(self, item, start_price, duration):
        # Create a new auction with the given item, start price, and duration
        end_time = time.time() + duration
        new_auction = Auction(item, start_price, end_time)
        self.auctions.insert(new_auction)
        self.blockchain.add_block(f"New auction created: {item}")

    def place_bid(self, auction_item, bidder, amount):
        # Place a bid on the auction with the given item, bidder, and amount
        auction = self.auctions.search(lambda x: x.item == auction_item)
        if auction and auction.data.place_bid(bidder, amount):
            self.blockchain.add_block(f"Bid placed on {auction_item} by {bidder}: ${amount}")
            return True
        return False

    def end_auction(self, auction_item):
        # End the auction with the given item and determine the winner
        auction = self.auctions.search(lambda x: x.item == auction_item)
        if auction and time.time() >= auction.data.end_time:
            winner = auction.data.bids.tail.data if auction.data.bids.tail else None
            self.blockchain.add_block(f"Auction ended for {auction_item}. Winner: {winner[0] if winner else 'No winner'}")
            self.auctions.delete_node(auction.data)
            return winner
        return None


def main():
    # Main function to run the auction system
    auction_system = AuctionSystem()
    while True:
        print("\nBlockchain-based Auction System")
        print("1. Create a new auction")
        print("2. Place a bid")
        print("3. End an auction")
        print("4. View current auctions")
        print("5. Check blockchain validity")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            item = input("Enter the item name: ")
            start_price = float(input("Enter the starting price: "))
            duration = float(input("Enter the auction duration in hours: "))
            auction_system.create_auction(item, start_price, duration * 3600)
            print(f"Auction created for {item}")
        elif choice == '2':
            item = input("Enter the item name you want to bid on: ")
            bidder = input("Enter your name: ")
            amount = float(input("Enter your bid amount: "))
            if auction_system.place_bid(item, bidder, amount):
                print("Bid placed successfully")
            else:
                print("Failed to place bid. Make sure the auction exists and your bid is higher than the current price.")
        elif choice == '3':
            item = input("Enter the item name of the auction to end: ")
            winner = auction_system.end_auction(item)
            if winner:
                print(f"Auction for {item} ended. Winner: {winner[0]} with bid ${winner[1]}")
            else:
                print(f"Auction for {item} not yet ended or no valid bids.")
        elif choice == '4':
            print("Current auctions:")
            auction_system.auctions.traverse()
        elif choice == '5':
            print(f"Blockchain is valid: {auction_system.blockchain.is_chain_valid()}")
        elif choice == '6':
            print("Thank you for using the Blockchain-based Auction System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

