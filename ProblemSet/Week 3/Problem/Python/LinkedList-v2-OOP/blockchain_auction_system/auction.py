from blockchain_auction_system.double_ended_linked_list import DoubleEndedLinkedList


class Auction:
    """
    Represents an auction in the system.
    """
    def __init__(self, item, start_price, end_time):
        self.item = item
        self.start_price = start_price
        self.current_price = start_price
        self.end_time = end_time
        self.bids = DoubleEndedLinkedList()

    def place_bid(self, bidder, amount):
        """
        Place a bid in the auction.
        """
        if amount > self.current_price and time.time() < self.end_time:
            self.current_price = amount
            self.bids.insert_at_end((bidder, amount))
            return True
        return False