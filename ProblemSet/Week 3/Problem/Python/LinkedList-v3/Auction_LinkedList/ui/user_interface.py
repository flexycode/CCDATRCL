from services.auction_system import AuctionSystem
from models.auction_item import AuctionItem


class UserInterface:
    def __init__(self):
        self.auction_system = AuctionSystem()

    def display_menu(self):
        print("\n===== Auction System Menu =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Items")
        print("4. Place Bid")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.display_items()
            elif choice == "4":
                self.place_bid()
            elif choice == "5":
                print("Thank you for using the Auction System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter starting price: "))
        result = self.auction_system.add_item(AuctionItem(name, price))
        print(result)

    def remove_item(self):
        name = input("Enter item name to remove: ")
        result = self.auction_system.remove_item(name)
        print(result)

    def display_items(self):
        print("\nCurrent Auction Items:")
        items = self.auction_system.display_items()
        if items:
            for item in items:
                print(item)
        else:
            print("No items in the auction")

    def place_bid(self):
        name = input("Enter item name: ")
        bidder = input("Enter your name: ")
        amount = float(input("Enter bid amount: "))
        result = self.auction_system.place_bid(name, bidder, amount)
        print(result)

        # Display updated item information
        item = self.auction_system.get_item(name)
        if item:
            print(f"Updated item information: {item}")