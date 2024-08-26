def main():
    # Create a list to store K-POP groups
    kpop = []

    # Ask the user to enter the number of K-POP groups to add to the list
    num_groups = int(input("Enter the number of K-POP groups to add to the list: "))

    # Ask the user to enter the K-POP groups to add to the list
    print("Enter the K-POP groups to add to the list:")
    for i in range(num_groups):
        group = input(f"Group {i+1}: ")
        kpop.append(group)

    # Print the list elements
    print("List KPOP:")
    for group in kpop:
        print(group, end=" ")
    print()

    # Ask the user if they want to remove a K-POP group from the list
    remove_group = input("Do you want to remove a K-POP group from the list? (yes/no): ")
    if remove_group.lower() == "yes":
        
        # Ask the user to enter the K-POP group to remove
        group_to_remove = input("Enter the K-POP group to remove: ")
        if group_to_remove in kpop:
            kpop.remove(group_to_remove)
            print("Updated list KPOP:")
            for group in kpop:
                print(group, end=" ")
            print()
        else:
            print("Group not found in the list.")
    else:
        print("No K-POP group removed from the list.")

    # Ask the user if they want to add another K-POP group to the list
    add_group = input("Do you want to add another K-POP group to the list? (yes/no): ")
    if add_group.lower() == "yes":
        
        # Ask the user to enter the new K-POP group
        new_group = input("Enter the new K-POP group: ")
        kpop.append(new_group)
        print("Updated list KPOP:")
        for group in kpop:
            print(group, end=" ")
        print()
    else:
        print("No new K-POP group added to the list.")

if __name__ == "__main__":
    main()
