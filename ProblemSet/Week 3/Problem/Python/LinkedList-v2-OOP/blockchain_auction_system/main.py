from auction_system import AuctionSystem


def main():
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