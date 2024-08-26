function main() {
    // Ask the user to enter the size of the array
    let size = parseInt(prompt("Enter the size of the array: "));

    // Declare and initialize an array of integers with the specified size
    let scores = [];

    // Ask the user to enter the values for the array elements
    console.log("Enter the values for the array elements:");
    for (let i = 0; i < size; i++) {
        while (true) {
            let score = prompt(`Element ${i + 1}: `);
            if (!isNaN(score)) {
                scores.push(parseInt(score));
                break;
            } else {
                console.log("Invalid input. Please enter a valid integer.");
            }
        }
    }

    // Print the array elements
    console.log("Array elements:");
    for (let score of scores) {
        console.log(score + " ");
    }
    console.log();

    // Ask the user if they want to add or remove an element from the array
    while (true) {
        let inputStr = prompt("Do you want to add or remove an element from the array? (add/remove): ");
        if (inputStr.toLowerCase() === "add" || inputStr.toLowerCase() === "remove") {
            break;
        } else {
            console.log("Invalid input. Please enter 'add' or 'remove'.");
        }
    }

    if (inputStr.toLowerCase() === "add") {
        // Ask the user to enter the new element
        while (true) {
            let newElement = prompt("Enter the new element: ");
            if (!isNaN(newElement)) {
                scores.push(parseInt(newElement));
                break;
            } else {
                console.log("Invalid input. Please enter a valid integer.");
            }
        }

        // Print the updated array elements
        console.log("Updated array elements:");
        for (let score of scores) {
            console.log(score + " ");
        }
        console.log();
    } else if (inputStr.toLowerCase() === "remove") {
        // Ask the user to enter the index of the element to remove
        while (true) {
            let index = prompt("Enter the index of the element to remove: ");
            if (!isNaN(index) && 0 <= parseInt(index) < scores.length) {
                scores.splice(parseInt(index), 1);
                break;
            } else {
                console.log("Invalid index. Please enter a valid index.");
            }
        }

        // Print the updated array elements
        console.log("Updated array elements:");
        for (let score of scores) {
            console.log(score + " ");
        }
        console.log();
    }
}

main();
