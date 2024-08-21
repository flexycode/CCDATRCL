# Example program that demonstrates the use of a Stack (using List)
def stack_example():
    # Create a Stack of integers
    stack = []

    # Push elements onto the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)

    # Print the stack elements
    print("Stack elements:")
    print(stack)

    # Pop an element from the stack
    popped_element = stack.pop()
    print("Popped element:")
    print(popped_element)

    # Print the updated stack elements
    print("Updated stack elements:")
    print(stack)

stack_example()
