kpop = []

# Ask the user to enter the number of K-POP groups to add to the list
num_groups = int(input("Enter the number of K-POP groups to add to the list: "))

# Ask the user to enter the K-POP groups to add to the list
for i in range(num_groups):
    group = input(f"Group {i + 1}: ")
    kpop.append(group)

# Print the list elements
print("List KPOP:")
print(" ".join(kpop))

# Ask the user if they want to remove a K-POP group from the list
input_str = input("Do you want to remove a K-POP group from the list? (yes/no): ")

if input_str.lower() == "yes":
    # Ask the user to enter the K-POP group to remove
    remove_group = input("Enter the K-POP group to remove: ")
    if remove_group in kpop:
        kpop.remove(remove_group)

    # Print the updated list elements
    print("Updated list KPOP:")
    print(" ".join(kpop))
else:
    print("No K-POP group removed from the list.")

# Ask the user if they want to add another K-POP group to the list
input_str = input("Do you want to add another K-POP group to the list? (yes/no): ")

if input_str.lower() == "yes":
    # Ask the user to enter the new K-POP group
    new_group = input("Enter the new K-POP group: ")
    kpop.append(new_group)

    # Print the updated list elements
    print("Updated list KPOP:")
    print(" ".join(kpop))
else:
    print("No new K-POP group added to the list.")
