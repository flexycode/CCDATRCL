class Node:
    """
    Basic node structure for linked lists.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For doubly linked list