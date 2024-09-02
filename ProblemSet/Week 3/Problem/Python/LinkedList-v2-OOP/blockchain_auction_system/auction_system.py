from blockchain import Blockchain
from circular_linked_list import CircularLinkedList
from auction import Auction
import time

class AuctionSystem:
    """
    Manages the entire auction system.
    """
    def __init__(self):
        self.blockchain = Blockchain()
        self.auctions = CircularLinkedList()

    def create_auction(self, item, start_price, duration):
        """
        Create a new auction.
        """
        end_time = time.time() + duration
        new_auction = Auction(item, start_price, end_time)
        self.auctions.insert(new_auction)
        self.blockchain.add_block(f"New auction created: {item}")

    def place_bid(self, auction_item, bidder, amount):
        """
        Place a bid on an auction.
        """
        auction = self.auctions.search(lambda x: x.item == auction_item)
        if auction and auction.data.place_bid(bidder, amount):
            self.blockchain.add_block(f"Bid placed on {auction_item} by {bidder}: ${amount}")
            return True
        return False

    def end_auction(self, auction_item):
        """
        End an auction and determine the winner.
        """
        auction = self.auctions.search(lambda x: x.item == auction_item)
        if auction and time.time() >= auction.data.end_time:
            winner = auction.data.bids.tail.data if auction.data.bids.tail else None
            self.blockchain.add_block(f"Auction ended for {auction_item}. Winner: {winner[0] if winner else 'No winner'}")
            self.auctions.delete_node(auction.data)
            return winner
        return None