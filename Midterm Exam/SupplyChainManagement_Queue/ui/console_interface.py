from services.warehouse_manager import WarehouseManager
from models.item import Item

class ConsoleInterface:
    def __init__(self, capacity):
        self.warehouse = WarehouseManager(capacity)

    @staticmethod
    def display_menu():
        print("\n===== Supply Chain Management System =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Next Item")
        print("4. Check Warehouse Status")
        print("5. Display All Items")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.view_next_item()
            elif choice == "4":
                self.check_warehouse_status()
            elif choice == "5":
                self.display_all_items()
            elif choice == "6":
                print("Thank you for using the Supply Chain Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_item(self):
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        item = Item(item_id, name, quantity)
        result = self.warehouse.add_item(item)
        print(result)

    def remove_item(self):
        result = self.warehouse.remove_item()
        print(result)

    def view_next_item(self):
        result = self.warehouse.view_next_item()
        print(result)

    def check_warehouse_status(self):
        if self.warehouse.is_warehouse_full():
            print("Warehouse is full.")
        else:
            print("Warehouse has space available.")

    def display_all_items(self):
        items = self.warehouse.display_items()
        print("Items in the warehouse:")
        print(items)



