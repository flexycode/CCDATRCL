from models.node import Node

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def delete(self, item_name):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.item.name.lower() == item_name.lower():
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def search(self, item_name):
        if not self.head:
            return None

        current = self.head
        while True:
            if current.item.name.lower() == item_name.lower():
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def traverse(self):
        items = []
        if not self.head:
            return items

        current = self.head
        while True:
            items.append(current.item)
            current = current.next
            if current == self.head:
                break
        return items