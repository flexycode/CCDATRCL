from node import Node

class DoubleEndedLinkedList:
    """
    Double-ended linked list implementation.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        """
        Delete a node with the given key.
        Time Complexity: O(n)
        """
        if not self.head:
            return

        if self.head.data == key:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return

        current = self.head
        while current.next:
            if current.next.data == key:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
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
            print(current.data, end=" -> ")
            current = current.next
        print("None")
