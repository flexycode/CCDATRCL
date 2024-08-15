function isPalindrome(str) {
    // Check if the string is equal to its reverse
    return str === str.split("").reverse().join("");
}

// Define the string to check
let str = "madam";

// Check if the string is a palindrome
if (isPalindrome(str)) {
    // If it's a palindrome, log a message to the console
    console.log("The string is a palindrome.");
} else {
    // If it's not a palindrome, log a message to the console
    console.log("The string is not a palindrom.");