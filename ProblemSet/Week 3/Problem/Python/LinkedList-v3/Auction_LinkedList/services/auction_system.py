from data_structures.circular_doubly_linked_list import CircularDoublyLinkedList
from models.auction_item import AuctionItem

class AuctionSystem:
    def __init__(self):
        self.items = CircularDoublyLinkedList()

    def add_item(self, item):
        self.items.insert(item)
        return "Item added successfully"

    def remove_item(self, item_name):
        if self.items.delete(item_name):
            return "Item removed successfully"
        return "Item not found"

    def display_items(self):
        return self.items.traverse()

    def place_bid(self, item_name, bidder, bid_amount):
        item_node = self.items.search(item_name)
        if item_node:
            item = item_node.item
            if bid_amount > item.current_price:
                item.current_price = bid_amount
                item.highest_bidder = bidder
                return f"Bid placed successfully for {item.name}"
            else:
                return "Bid amount must be higher than the current price"
        else:
            return "Item not found"

    def get_item(self, item_name):
        item_node = self.items.search(item_name)
        return item_node.item if item_node else None