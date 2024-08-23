/**
 * Checks if a given string is a palindrome.
 * 
 * A palindrome is a string that reads the same backward as forward.
 * This function ignores case, spaces, and punctuation when checking for palindromes.
 * 
 * @param {string} s the input string to check
 * @returns {boolean} true if the string is a palindrome, false otherwise
 */
function isPalindrome(s) {
  // Remove non-alphanumeric characters and convert to lowercase
  // This is done to ignore case, spaces, and punctuation when checking for palindromes
  s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

  // Check if the string is equal to its reverse
  // This is the core logic of checking if a string is a palindrome
  const reversed = s.split('').reverse().join('');
  return s === reversed;
}

/**
 * Asks the user to input a string and checks if it's a palindrome.
 */
function main() {
  // Prompt the user to input a string
  const inputString = prompt("Enter a string to check if it's a palindrome:");

  // Check if the input string is a palindrome
  if (isPalindrome(inputString)) {
    // If it's a palindrome, print a success message
    console.log("The string is a palindrome.");
  } else {
    // If it's not a palindrome, print a failure message
    console.log("The string is not a palindrome.");
  }
}

// Call the main function to start the program
main();
