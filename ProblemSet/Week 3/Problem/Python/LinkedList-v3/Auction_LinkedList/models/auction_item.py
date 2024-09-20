class AuctionItem:
    def __init__(self, name, starting_price):
        self.name = name
        self.starting_price = starting_price
        self.current_price = starting_price
        self.highest_bidder = None

    def __str__(self):
        return f"{self.name} - Current Price: ${self.current_price:.2f} - Highest Bidder: {self.highest_bidder or 'None'}"