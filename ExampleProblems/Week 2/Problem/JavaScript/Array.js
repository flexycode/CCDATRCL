let scores = [];

// Ask the user to enter the size of the array
let size = parseInt(prompt("Enter the size of the array: "));

// Ask the user to enter the values for the array elements
for (let i = 0; i < size; i++) {
  let element = parseInt(prompt(`Element ${i + 1}: `));
  scores.push(element);
}

// Print the array elements
console.log("Array elements:");
console.log(scores.join(" "));

// Ask the user if they want to add or remove an element from the array
let input = prompt("Do you want to add or remove an element from the array? (add/remove): ");

if (input.toLowerCase() === "add") {
  // Ask the user to enter the new element
  let newElement = parseInt(prompt("Enter the new element: "));
  scores.push(newElement);

  // Print the updated array elements
  console.log("Updated array elements:");
  console.log(scores.join(" "));
} else if (input.toLowerCase() === "remove") {
  
  // Ask the user to enter the index of the element to remove
  let index = parseInt(prompt("Enter the index of the element to remove: "));
  scores.splice(index, 1);

  // Print the updated array elements
  console.log("Updated array elements:");
  console.log(scores.join(" "));
}
