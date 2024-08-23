// Example program that demonstrates the use of a Stack (using Array)
const stackExample = () => {
  // Create a Stack of integers
  let stack = [];

  // Push elements onto the stack
  stack.push(1);
  stack.push(2);
  stack.push(3);
  stack.push(4);
  stack.push(5);

  // Print the stack elements
  console.log("Stack elements:");
  console.log(stack);

  // Pop an element from the stack
  let poppedElement = stack.pop();
  console.log("Popped element:");
  console.log(poppedElement);

  // Print the updated stack elements
  console.log("Updated stack elements:");
  console.log(stack);
};

stackExample();
