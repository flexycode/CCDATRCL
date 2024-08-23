let stack = [];

// Ask the user to enter the number of elements to push onto the stack
let numElements = parseInt(prompt("Enter the number of elements to push onto the stack: "));

// Ask the user to enter the elements to push onto the stack
for (let i = 0; i < numElements; i++) {
  let element = parseInt(prompt(`Element ${i + 1}: `));
  stack.push(element);
}

// Print the stack elements
console.log("Stack elements:");
console.log(stack);

// Ask the user if they want to pop an element from the stack
let input = prompt("Do you want to pop an element from the stack? (yes/no): ");

if (input.toLowerCase() === "yes") {
  // Pop an element from the stack
  let poppedElement = stack.pop();

  // Print the popped element
  console.log("Popped element: " + poppedElement);

  // Print the updated stack elements
  console.log("Updated stack elements:");
  console.log(stack);
} else {
  console.log("No element popped from the stack.");
}

// Ask the user if they want to push another element onto the stack
input = prompt("Do you want to push another element onto the stack? (yes/no): ");

if (input.toLowerCase() === "yes") {
  // Ask the user to enter the new element
  let newElement = parseInt(prompt("Enter the new element: "));
  stack.push(newElement);

  // Print the updated stack elements
  console.log("Updated stack elements:");
  console.log(stack);
} else {
  console.log("No new element pushed onto the stack.");
}
