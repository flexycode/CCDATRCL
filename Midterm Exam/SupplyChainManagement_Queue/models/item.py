class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item(id={self.item_id}, name={self.name}, quantity={self.quantity})"

