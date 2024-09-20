from data_structures.circular_queue import CircularQueue

class WarehouseManager:
    def __init__(self, capacity):
        self.storage = CircularQueue(capacity)

    def add_item(self, item):
        if self.storage.enqueue(item):
            return f"Item {item.name} added successfully."
        return "Warehouse is full. Cannot add more items."

    def remove_item(self):
        item = self.storage.dequeue()
        if item:
            return f"Removed item: {item}"
        return "Warehouse is empty. No items to remove."

    def view_next_item(self):
        item = self.storage.peek()
        if item:
            return f"Next item to be removed: {item}"
        return "Warehouse is empty. No items to view."

    def is_warehouse_full(self):
        return self.storage.is_full()

    def display_items(self):
        items = self.storage.display()
        if items:
            return "\n".join(str(item) for item in items)
        return "Warehouse is empty."



