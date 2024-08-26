def main():
    
    # Ask the user to enter the size of the array
    size = int(input("Enter the size of the array: "))

    # Declare and initialize an array of integers with the specified size
    scores = []

    # Ask the user to enter the values for the array elements
    print("Enter the values for the array elements:")
    for i in range(size):
        while True:
            try:
                score = int(input(f"Element {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Print the array elements
    print("Array elements:")
    for score in scores:
        print(score, end=" ")
    print()

    # Ask the user if they want to add or remove an element from the array
    while True:
        input_str = input("Do you want to add or remove an element from the array? (add/remove): ")
        if input_str.lower() == "add" or input_str.lower() == "remove":
            break
        else:
            print("Invalid input. Please enter 'add' or 'remove'.")

    if input_str.lower() == "add":
        # Ask the user to enter the new element
        while True:
            try:
                new_element = int(input("Enter the new element: "))
                scores.append(new_element)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Print the updated array elements
        print("Updated array elements:")
        for score in scores:
            print(score, end=" ")
        print()
    elif input_str.lower() == "remove":
        # Ask the user to enter the index of the element to remove
        while True:
            try:
                index = int(input("Enter the index of the element to remove: "))
                if 0 <= index < len(scores):
                    scores.pop(index)
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Print the updated array elements
        print("Updated array elements:")
        for score in scores:
            print(score, end=" ")
        print()

if __name__ == "__main__":
    main()
