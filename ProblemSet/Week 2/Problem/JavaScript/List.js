// Example program that demonstrates the use of a List (using Array)
const listExample = () => {
  // Create a List of strings
  let colors = ["Red", "Green", "Blue", "Yellow"];

  // Print the list elements
  console.log("List elements:");
  console.log(colors);

  // Add an element to the list
  colors.push("Purple");
  console.log("Updated list elements:");
  console.log(colors);

  // Remove an element from the list
  colors.splice(colors.indexOf("Green"), 1);
  console.log("Updated list elements:");
  console.log(colors);
};

listExample();
