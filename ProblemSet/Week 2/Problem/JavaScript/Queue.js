// Example program that demonstrates the use of a Queue (using Array)
const queueExample = () => {
  // Create a Queue of strings
  let queue = [];

  // Add elements to the queue
  queue.push("Apple");
  queue.push("Banana");
  queue.push("Cherry");
  queue.push("Date");

  // Print the queue elements
  console.log("Queue elements:");
  console.log(queue);

  // Remove an element from the front of the queue
  let removedElement = queue.shift();
  console.log("Removed element:");
  console.log(removedElement);

  // Print the updated queue elements
  console.log("Updated queue elements:");
  console.log(queue);
};

queueExample();
