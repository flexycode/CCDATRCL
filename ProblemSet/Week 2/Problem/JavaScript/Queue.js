let queue = [];

/**
 * Displays the queue menu to the user
 */
function displayMenu() {
  console.log("Queue Menu:");
  console.log("1. Add elements to the queue");
  console.log("2. Remove an element from the front of the queue");
  console.log("3. Add another element to the queue");
  console.log("4. Exit");
}

/**
 * Adds elements to the queue
 */
function addElementsToQueue() {
  // Ask the user to enter the number of elements to add to the queue
  let numElements = parseInt(prompt("Enter the number of elements to add to the queue: "));

  // Add elements to the queue
  for (let i = 0; i < numElements; i++) {
    let element = prompt(`Element ${i + 1}: `);
    queue.push(element);
  }

  // Print the queue elements
  console.log("Queue elements:");
  console.log(queue);
}

/**
 * Removes an element from the front of the queue
 */
function removeElementFromFront() {
  // Check if the queue is not empty
  if (queue.length > 0) {
    // Remove an element from the front of the queue
    let removedElement = queue.shift();
    console.log("Removed element: " + removedElement);
    console.log("Updated queue elements:");
    console.log(queue);
  } else {
    console.log("Queue is empty. Cannot remove an element.");
  }
}

/**
 * Adds another element to the queue
 */
function addAnotherElementToQueue() {
  // Ask the user to enter the new element
  let newElement = prompt("Enter the new element: ");
  queue.push(newElement);
  console.log("Updated queue elements:");
  console.log(queue);
}

let choice;
do {
  displayMenu();
  choice = parseInt(prompt("Enter your choice: "));

  switch (choice) {
    case 1:
      addElementsToQueue();
      break;
    case 2:
      removeElementFromFront();
      break;
    case 3:
      addAnotherElementToQueue();
      break;
    case 4:
      console.log("Exiting...");
      break;
    default:
      console.log("Invalid choice. Please try again.");
  }
} while (choice !== 4);
