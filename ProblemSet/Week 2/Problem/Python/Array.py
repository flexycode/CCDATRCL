scores = []

# Ask the user to enter the size of the array
size = int(input("Enter the size of the array: "))

# Ask the user to enter the values for the array elements
for i in range(size):
    element = int(input(f"Element {i + 1}: "))
    scores.append(element)

# Print the array elements
print("Array elements:")
print(" ".join(map(str, scores)))

# Ask the user if they want to add or remove an element from the array
input_str = input("Do you want to add or remove an element from the array? (add/remove): ")

if input_str.lower() == "add":
  
    # Ask the user to enter the new element
    new_element = int(input("Enter the new element: "))
    scores.append(new_element)

    # Print the updated array elements
    print("Updated array elements:")
    print(" ".join(map(str, scores)))
elif input_str.lower() == "remove":
  
    # Ask the user to enter the index of the element to remove
    index = int(input("Enter the index of the element to remove: "))
    del scores[index]

    # Print the updated array elements
    print("Updated array elements:")
    print(" ".join(map(str, scores)))
