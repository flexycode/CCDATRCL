from node import Node

class CircularLinkedList:
    """
    Circular linked list implementation.
    """
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Insert a new node into the circular linked list.
        Time Complexity: O(1) if inserting at the beginning, O(n) if inserting at the end
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        """
        Delete a node with the given key.
        Time Complexity: O(n)
        """
        if not self.head:
            return

        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        if current.data == key:
            prev.next = self.head

    def search(self, key):
        """
        Search for a node with the given key.
        Time Complexity: O(n)
        """
        if not self.head:
            return None

        current = self.head
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def traverse(self):
        """
        Traverse and print all nodes in the list.
        Time Complexity: O(n)
        """
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (back to head)")