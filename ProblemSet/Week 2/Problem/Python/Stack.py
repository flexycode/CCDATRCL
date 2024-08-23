stack = []

# Ask the user to enter the number of elements to push onto the stack
num_elements = int(input("Enter the number of elements to push onto the stack: "))

# Ask the user to enter the elements to push onto the stack
for i in range(num_elements):
    element = int(input(f"Element {i + 1}: "))
    stack.append(element)

# Print the stack elements
print("Stack elements:")
print(stack)

# Ask the user if they want to pop an element from the stack
input_str = input("Do you want to pop an element from the stack? (yes/no): ")

if input_str.lower() == "yes":
    # Pop an element from the stack
    if stack:
        popped_element = stack.pop()
        print("Popped element: " + str(popped_element))
    else:
        print("Stack is empty. Cannot pop an element.")

    # Print the updated stack elements
    print("Updated stack elements:")
    print(stack)
else:
    print("No element popped from the stack.")

# Ask the user if they want to push another element onto the stack
input_str = input("Do you want to push another element onto the stack? (yes/no): ")

if input_str.lower() == "yes":
    # Ask the user to enter the new element
    new_element = int(input("Enter the new element: "))
    stack.append(new_element)

    # Print the updated stack elements
    print("Updated stack elements:")
    print(stack)
else:
    print("No new element pushed onto the stack.")
