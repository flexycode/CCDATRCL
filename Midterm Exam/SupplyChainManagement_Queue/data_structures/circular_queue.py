class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            return False
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return []
        items = []
        index = self.front
        for _ in range(self.size):
            items.append(self.queue[index])
            index = (index + 1) % self.capacity
        return items