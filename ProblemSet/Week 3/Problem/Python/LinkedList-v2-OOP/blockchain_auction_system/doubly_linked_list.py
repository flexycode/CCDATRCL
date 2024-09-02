from node import Node

class DoublyLinkedList:
    """
    Doubly linked list implementation.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, key):
        """
        Delete a node with the given key.
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def search(self, key):
        """
        Search for a node with the given key.
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def traverse(self):
        """
        Traverse and print all nodes in the list.
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def insert_at_end(self, genesis_block):
        pass