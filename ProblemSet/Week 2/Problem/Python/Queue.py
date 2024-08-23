queue = []

def display_menu():
  print("Queue Menu:")
  print("1. Add elements to the queue")
  print("2. Remove an element from the front of the queue")
  print("3. Add another element to the queue")
  print("4. Exit")

def add_elements_to_queue():
  num_elements = int(input("Enter the number of elements to add to the queue: "))

  for i in range(num_elements):
    element = input(f"Element {i + 1}: ")
    queue.append(element)

  print("Queue elements:")
  print(queue)

def remove_element_from_front():
  if queue:
    removed_element = queue.pop(0)
    print("Removed element: " + removed_element)
    print("Updated queue elements:")
    print(queue)
  else:
    print("Queue is empty. Cannot remove an element.")

def add_another_element_to_queue():
  new_element = input("Enter the new element: ")
  queue.append(new_element)
  print("Updated queue elements:")
  print(queue)

while True:
  display_menu()
  choice = int(input("Enter your choice: "))

  if choice == 1:
    add_elements_to_queue()
  elif choice == 2:
    remove_element_from_front()
  elif choice == 3:
    add_another_element_to_queue()
  elif choice == 4:
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
