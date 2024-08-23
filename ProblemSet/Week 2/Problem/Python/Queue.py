# Example program that demonstrates the use of a Queue using deque from collections module
from collections import deque

def queue_example():
    # Create a Queue of strings
    queue = deque(["Apple", "Banana", "Cherry", "Date"])

    # Print the queue elements
    print("Queue elements:")
    print(queue)

    # Add an element to the queue
    queue.append("Elderberry")
    print("Updated queue elements:")
    print(queue)

    # Remove an element from the front of the queue
    removed_element = queue.popleft()
    print("Removed element:")
    print(removed_element)

    # Print the updated queue elements
    print("Updated queue elements:")
    print(queue)

queue_example()

