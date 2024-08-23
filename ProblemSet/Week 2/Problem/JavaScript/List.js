let kpop = [];

// Ask the user to enter the number of K-POP groups to add to the list
let numGroups = parseInt(prompt("Enter the number of K-POP groups to add to the list: "));

// Ask the user to enter the K-POP groups to add to the list
for (let i = 0; i < numGroups; i++) {
  let group = prompt(`Group ${i + 1}: `);
  kpop.push(group);
}

// Print the list elements
console.log("List KPOP:");
console.log(kpop.join(" "));

// Ask the user if they want to remove a K-POP group from the list
let input = prompt("Do you want to remove a K-POP group from the list? (yes/no): ");

if (input.toLowerCase() === "yes") {
  // Ask the user to enter the K-POP group to remove
  let removeGroup = prompt("Enter the K-POP group to remove: ");
  let index = kpop.indexOf(removeGroup);
  if (index !== -1) {
    kpop.splice(index, 1);
  }

  // Print the updated list elements
  console.log("Updated list KPOP:");
  console.log(kpop.join(" "));
} else {
  console.log("No K-POP group removed from the list.");
}

// Ask the user if they want to add another K-POP group to the list
input = prompt("Do you want to add another K-POP group to the list? (yes/no): ");

if (input.toLowerCase() === "yes") {
  // Ask the user to enter the new K-POP group
  let newGroup = prompt("Enter the new K-POP group: ");
  kpop.push(newGroup);

  // Print the updated list elements
  console.log("Updated list KPOP:");
  console.log(kpop.join(" "));
} else {
  console.log("No new K-POP group added to the list.");
}
